"use client";

import { useEffect, useRef, useMemo } from "react";
import { Canvas, useFrame, useThree } from "@react-three/fiber";
import * as THREE from "three";

/* ── Camera ── */
function CameraSync() {
    const { camera, size } = useThree();
    useEffect(() => {
        const c = camera as THREE.OrthographicCamera;
        c.left = -size.width / 2;
        c.right = size.width / 2;
        c.top = size.height / 2;
        c.bottom = -size.height / 2;
        c.updateProjectionMatrix();
    }, [camera, size]);
    return null;
}

/* ── Flight path (purely time-based) ── */
function getPos(t: number) {
    const s = 0.15;
    const x = 50 + 28 * Math.sin(t * s * 3.2) + 10 * Math.sin(t * s * 7.1);
    const y = 48 + 18 * Math.sin(t * s * 4.5) + 7 * Math.cos(t * s * 9.3);
    return { x, y };
}

/* ── Trail colors gradient ── */
const TRAIL_COLORS = [
    "#fbbf24", "#f59e0b", "#22d3ee", "#06b6d4", "#a78bfa",
    "#c084fc", "#818cf8", "#34d399", "#22d3ee", "#f472b6",
];
function trailColor(i: number) { return TRAIL_COLORS[i % TRAIL_COLORS.length]; }

/* ── Comet Trail (lightweight, no UFO) ── */
function Trail() {
    const MAX = 30; // reduced from 60 for perf
    const meshRefs = useRef<(THREE.Mesh | null)[]>([]);
    const glowRefs = useRef<(THREE.Mesh | null)[]>([]);
    const positions = useRef<THREE.Vector3[]>(Array.from({ length: MAX }, () => new THREE.Vector3(9999, 9999, 0)));
    const tick = useRef(0);
    const { size } = useThree();
    const items = useMemo(() => Array.from({ length: MAX }), []);

    // Shared geometries (reuse instead of creating per-mesh)
    const coreGeo = useMemo(() => new THREE.SphereGeometry(1, 6, 6), []);
    const glowGeo = useMemo(() => new THREE.SphereGeometry(1, 4, 4), []);

    useFrame(() => {
        tick.current++;
        if (tick.current % 3 !== 0) return; // update every 3rd frame

        const t = performance.now() / 1000;
        const p = getPos(t);
        const wx = (p.x / 100) * size.width - size.width / 2;
        const wy = -((p.y / 100) * size.height - size.height / 2);
        for (let i = MAX - 1; i > 0; i--) positions.current[i].copy(positions.current[i - 1]);
        positions.current[0].set(wx, wy, 0);

        for (let i = 0; i < MAX; i++) {
            const fade = 1 - i / MAX;
            const fadeQ = fade * fade;

            const m = meshRefs.current[i];
            if (m) {
                m.position.copy(positions.current[i]);
                m.scale.setScalar(fadeQ * 5);
                (m.material as THREE.MeshBasicMaterial).opacity = fadeQ * 0.6;
            }
            const g = glowRefs.current[i];
            if (g) {
                g.position.copy(positions.current[i]);
                g.scale.setScalar(fadeQ * 10);
                (g.material as THREE.MeshBasicMaterial).opacity = fadeQ * 0.1;
            }
        }
    });

    return (
        <>
            {items.map((_, i) => (
                <group key={i}>
                    <mesh ref={(el) => { meshRefs.current[i] = el; }} geometry={coreGeo}>
                        <meshBasicMaterial color={trailColor(i)} transparent opacity={0} depthWrite={false} />
                    </mesh>
                    <mesh ref={(el) => { glowRefs.current[i] = el; }} geometry={glowGeo}>
                        <meshBasicMaterial color={trailColor(i)} transparent opacity={0} depthWrite={false} />
                    </mesh>
                </group>
            ))}
        </>
    );
}

/* ── Comet Head (bright leading dot) ── */
function CometHead() {
    const ref = useRef<THREE.Mesh>(null);
    const glowRef = useRef<THREE.Mesh>(null);
    const { size } = useThree();

    useFrame(() => {
        const t = performance.now() / 1000;
        const p = getPos(t);
        const wx = (p.x / 100) * size.width - size.width / 2;
        const wy = -((p.y / 100) * size.height - size.height / 2);

        if (ref.current) {
            ref.current.position.set(wx, wy, 0);
            const pulse = 1 + Math.sin(t * 8) * 0.2;
            ref.current.scale.setScalar(4 * pulse);
        }
        if (glowRef.current) {
            glowRef.current.position.set(wx, wy, 0);
            const pulse = 1 + Math.sin(t * 6) * 0.3;
            glowRef.current.scale.setScalar(12 * pulse);
        }
    });

    return (
        <>
            {/* Bright core */}
            <mesh ref={ref}>
                <sphereGeometry args={[1, 8, 8]} />
                <meshBasicMaterial color="#ffffff" transparent opacity={0.9} depthWrite={false} />
            </mesh>
            {/* Soft glow halo */}
            <mesh ref={glowRef}>
                <sphereGeometry args={[1, 6, 6]} />
                <meshBasicMaterial color="#22d3ee" transparent opacity={0.15} depthWrite={false} />
            </mesh>
        </>
    );
}

/* ── Scene (comet only — no UFO, no lights needed) ── */
function Scene() {
    return (
        <>
            <CameraSync />
            <CometHead />
            <Trail />
        </>
    );
}

/* ── Main ── */
export default function ScrollCompanion() {
    const containerRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const el = containerRef.current;
        if (!el) return;
        const timer = setTimeout(() => { el.style.opacity = "1"; }, 600);
        return () => { clearTimeout(timer); };
    }, []);

    return (
        <div
            ref={containerRef}
            style={{
                position: "fixed", inset: 0, pointerEvents: "none",
                zIndex: 40, opacity: 0, transition: "opacity 1s ease-out",
            }}
        >
            <Canvas
                orthographic
                camera={{ zoom: 1, position: [0, 0, 100], near: 0.1, far: 200 }}
                gl={{ alpha: true, antialias: false, powerPreference: "high-performance" }}
                style={{ background: "transparent", pointerEvents: "none" }}
                frameloop="always"
            >
                <Scene />
            </Canvas>
        </div>
    );
}
