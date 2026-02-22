"use client";

import { useEffect, useRef } from "react";

export default function CursorGlow() {
    const glowRef = useRef<HTMLDivElement>(null);

    useEffect(() => {
        const el = glowRef.current;
        if (!el) return;

        let x = 0, y = 0, cx = 0, cy = 0;
        let rafId = 0;
        let running = false;

        const animate = () => {
            cx += (x - cx) * 0.08;
            cy += (y - cy) * 0.08;
            el.style.transform = `translate3d(${cx}px, ${cy}px, 0)`;

            // Stop loop when cursor is basically settled
            if (Math.abs(x - cx) < 0.5 && Math.abs(y - cy) < 0.5) {
                running = false;
                return;
            }
            rafId = requestAnimationFrame(animate);
        };

        const onMove = (e: MouseEvent) => {
            x = e.clientX;
            y = e.clientY;
            if (!running) {
                running = true;
                rafId = requestAnimationFrame(animate);
            }
        };

        window.addEventListener("mousemove", onMove);
        return () => {
            window.removeEventListener("mousemove", onMove);
            cancelAnimationFrame(rafId);
        };
    }, []);

    return <div ref={glowRef} className="cursor-glow hidden md:block" />;
}
