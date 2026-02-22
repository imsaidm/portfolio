"use client";

import { useEffect, useRef, useState, useCallback } from "react";
import { motion } from "framer-motion";
import { siteConfig, typingTexts } from "@/data/portfolio";
import MagneticButton from "./MagneticButton";

/* ─── Particle Canvas ─── */
function ParticleCanvas() {
    const canvasRef = useRef<HTMLCanvasElement>(null);
    const mouseRef = useRef({ x: 0, y: 0 });

    useEffect(() => {
        const canvas = canvasRef.current;
        if (!canvas) return;
        const ctx = canvas.getContext("2d");
        if (!ctx) return;

        let animId: number;
        let isVisible = true;
        let tick = 0;
        let particles: {
            x: number;
            y: number;
            vx: number;
            vy: number;
            size: number;
            opacity: number;
            hue: number;
        }[] = [];

        // Pause when hero is off-screen
        const observer = new IntersectionObserver(
            ([entry]) => { isVisible = entry.isIntersecting; },
            { threshold: 0 }
        );
        observer.observe(canvas);

        const resize = () => {
            canvas.width = window.innerWidth;
            canvas.height = window.innerHeight;
        };
        resize();
        window.addEventListener("resize", resize);

        const count = Math.min(40, Math.floor(window.innerWidth / 25));
        for (let i = 0; i < count; i++) {
            particles.push({
                x: Math.random() * canvas.width,
                y: Math.random() * canvas.height,
                vx: (Math.random() - 0.5) * 0.3,
                vy: (Math.random() - 0.5) * 0.3,
                size: Math.random() * 2 + 0.5,
                opacity: Math.random() * 0.5 + 0.1,
                hue: Math.random() * 60 + 250,
            });
        }

        const onMouse = (e: MouseEvent) => {
            mouseRef.current = { x: e.clientX, y: e.clientY };
        };
        window.addEventListener("mousemove", onMouse);

        const draw = () => {
            animId = requestAnimationFrame(draw);
            tick++;
            // Skip every other frame when not visible, every frame when visible
            if (!isVisible) { if (tick % 4 !== 0) return; }
            else if (tick % 2 !== 0) return;

            ctx.clearRect(0, 0, canvas.width, canvas.height);

            for (let i = 0; i < particles.length; i++) {
                const p = particles[i];
                /* mouse repel */
                const dx = p.x - mouseRef.current.x;
                const dy = p.y - mouseRef.current.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 150) {
                    const force = (150 - dist) / 150;
                    p.vx += (dx / dist) * force * 0.15;
                    p.vy += (dy / dist) * force * 0.15;
                }

                p.x += p.vx;
                p.y += p.vy;
                p.vx *= 0.99;
                p.vy *= 0.99;

                if (p.x < 0) p.x = canvas.width;
                if (p.x > canvas.width) p.x = 0;
                if (p.y < 0) p.y = canvas.height;
                if (p.y > canvas.height) p.y = 0;

                ctx.beginPath();
                ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
                ctx.fillStyle = `hsla(${p.hue}, 80%, 70%, ${p.opacity})`;
                ctx.fill();

                /* connect nearby — reduced distance */
                if (isVisible) {
                    for (let j = i + 1; j < particles.length; j++) {
                        const p2 = particles[j];
                        const cdx = p.x - p2.x;
                        const cdy = p.y - p2.y;
                        const d = cdx * cdx + cdy * cdy; // squared distance — avoid sqrt
                        if (d < 6400) { // 80px squared
                            ctx.beginPath();
                            ctx.moveTo(p.x, p.y);
                            ctx.lineTo(p2.x, p2.y);
                            ctx.strokeStyle = `hsla(270, 60%, 60%, ${0.08 * (1 - Math.sqrt(d) / 80)})`;
                            ctx.lineWidth = 0.5;
                            ctx.stroke();
                        }
                    }
                }
            }
        };
        draw();

        return () => {
            cancelAnimationFrame(animId);
            observer.disconnect();
            window.removeEventListener("resize", resize);
            window.removeEventListener("mousemove", onMouse);
        };
    }, []);

    return (
        <canvas
            ref={canvasRef}
            className="absolute inset-0 z-0 pointer-events-none"
        />
    );
}

/* ─── Typing Effect ─── */
function useTypingEffect(texts: string[], typeSpeed = 80, deleteSpeed = 50, pause = 2000) {
    const [displayText, setDisplayText] = useState("");
    const [textIndex, setTextIndex] = useState(0);
    const [isDeleting, setIsDeleting] = useState(false);

    useEffect(() => {
        const current = texts[textIndex];
        let timeout: NodeJS.Timeout;

        if (!isDeleting && displayText === current) {
            timeout = setTimeout(() => setIsDeleting(true), pause);
        } else if (isDeleting && displayText === "") {
            setIsDeleting(false);
            setTextIndex((i) => (i + 1) % texts.length);
        } else {
            timeout = setTimeout(
                () => {
                    setDisplayText(
                        isDeleting
                            ? current.slice(0, displayText.length - 1)
                            : current.slice(0, displayText.length + 1)
                    );
                },
                isDeleting ? deleteSpeed : typeSpeed
            );
        }

        return () => clearTimeout(timeout);
    }, [displayText, textIndex, isDeleting, texts, typeSpeed, deleteSpeed, pause]);

    return displayText;
}

/* ─── Stats Counter ─── */
function StatCounter({ value, label }: { value: number; label: string }) {
    const [count, setCount] = useState(0);
    const ref = useRef<HTMLDivElement>(null);
    const counted = useRef(false);

    useEffect(() => {
        const el = ref.current;
        if (!el) return;

        const observer = new IntersectionObserver(
            ([entry]) => {
                if (entry.isIntersecting && !counted.current) {
                    counted.current = true;
                    let start = 0;
                    const duration = 2000;
                    const startTime = performance.now();

                    const animate = (now: number) => {
                        const elapsed = now - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        const eased = 1 - Math.pow(1 - progress, 4);
                        setCount(Math.floor(eased * value));
                        if (progress < 1) requestAnimationFrame(animate);
                    };
                    requestAnimationFrame(animate);
                }
            },
            { threshold: 0.5 }
        );

        observer.observe(el);
        return () => observer.disconnect();
    }, [value]);

    return (
        <div ref={ref} className="text-center">
            <div className="flex items-baseline justify-center gap-0.5">
                <span className="text-3xl md:text-4xl font-bold font-display tabular-nums">
                    {count}
                </span>
                <span className="text-accent-purple text-xl font-bold">+</span>
            </div>
            <span className="text-muted text-sm mt-1 block">{label}</span>
        </div>
    );
}

/* ─── Hero Section ─── */
export default function Hero() {
    const typedText = useTypingEffect(typingTexts);

    const nameLetters = "Said Mustaqim".split("");

    return (
        <section
            id="hero"
            className="relative min-h-screen flex items-center justify-center overflow-hidden"
        >
            {/* Animated Grid Background */}
            <motion.div
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ duration: 2, delay: 0.5 }}
                className="grid-bg"
            />

            {/* Central Spotlight */}
            <motion.div
                initial={{ opacity: 0, scale: 0.5 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ duration: 2, ease: "easeOut" }}
                className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 w-[800px] h-[800px] pointer-events-none"
                style={{
                    background: "radial-gradient(circle, rgba(168, 85, 247, 0.08) 0%, rgba(0, 240, 255, 0.03) 40%, transparent 70%)",
                }}
            />

            {/* Floating Gradient Orbs */}
            <motion.div
                initial={{ opacity: 0, scale: 0 }}
                animate={{ opacity: 0.15, scale: 1 }}
                transition={{ duration: 1.5, delay: 0.3 }}
                className="gradient-orb gradient-orb-purple absolute -top-20 -right-20 w-[400px] h-[400px]"
            />
            <motion.div
                initial={{ opacity: 0, scale: 0 }}
                animate={{ opacity: 0.12, scale: 1 }}
                transition={{ duration: 1.5, delay: 0.6 }}
                className="gradient-orb gradient-orb-cyan absolute -bottom-32 -left-20 w-[350px] h-[350px]"
                style={{ animationDelay: "3s" }}
            />
            <motion.div
                initial={{ opacity: 0, scale: 0 }}
                animate={{ opacity: 0.1, scale: 1 }}
                transition={{ duration: 1.5, delay: 0.9 }}
                className="gradient-orb gradient-orb-pink absolute top-1/3 -left-40 w-[300px] h-[300px]"
                style={{ animationDelay: "5s" }}
            />

            {/* Decorative Rotating Rings */}
            <div className="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2 pointer-events-none">
                <motion.div
                    initial={{ opacity: 0, scale: 0.5 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 1.5, delay: 0.8 }}
                    className="w-[500px] h-[500px] md:w-[700px] md:h-[700px] rounded-full border border-white/[0.03] absolute top-1/2 left-1/2 animate-[ring-rotate_30s_linear_infinite]"
                    style={{ transformOrigin: "center center" }}
                />
                <motion.div
                    initial={{ opacity: 0, scale: 0.5 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ duration: 1.5, delay: 1.0 }}
                    className="w-[600px] h-[600px] md:w-[850px] md:h-[850px] rounded-full border border-white/[0.02] absolute top-1/2 left-1/2 animate-[ring-rotate_45s_linear_infinite_reverse]"
                    style={{ transformOrigin: "center center" }}
                />
            </div>

            {/* Particle Canvas */}
            <ParticleCanvas />

            <div className="relative z-10 max-w-5xl mx-auto px-4 sm:px-6 text-center pt-20 md:pt-0">
                {/* Badge */}


                {/* Greeting */}
                <motion.p
                    initial={{ opacity: 0, y: 20, filter: "blur(10px)" }}
                    animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
                    transition={{ delay: 0.3, duration: 0.8 }}
                    className="text-muted text-lg mb-3 font-light"
                >
                    Hello, I&apos;m
                </motion.p>

                {/* Name with glow */}
                <div className="relative inline-block">
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        transition={{ delay: 0.8, duration: 1.5 }}
                        className="absolute inset-0 blur-3xl pointer-events-none"
                        style={{
                            background: "linear-gradient(135deg, rgba(168, 85, 247, 0.15), rgba(0, 240, 255, 0.1), rgba(236, 72, 153, 0.1))",
                        }}
                    />
                    <h1 className="relative text-4xl sm:text-5xl md:text-7xl lg:text-8xl font-display font-bold tracking-tighter mb-4 md:mb-6">
                        {nameLetters.map((letter, i) => (
                            <motion.span
                                key={i}
                                initial={{ opacity: 0, y: 60, rotateX: -90, filter: "blur(8px)" }}
                                animate={{ opacity: 1, y: 0, rotateX: 0, filter: "blur(0px)" }}
                                transition={{
                                    delay: 0.4 + i * 0.04,
                                    duration: 0.7,
                                    ease: [0.16, 1, 0.3, 1],
                                }}
                                className={`inline-block ${letter === " " ? "w-2 sm:w-4 md:w-6" : "hover:text-accent-purple transition-colors duration-200 cursor-default"
                                    }`}
                            >
                                {letter === " " ? "\u00A0" : letter}
                            </motion.span>
                        ))}
                    </h1>
                </div>

                {/* Typed tagline */}
                <motion.div
                    initial={{ opacity: 0, scale: 0.95 }}
                    animate={{ opacity: 1, scale: 1 }}
                    transition={{ delay: 1, duration: 0.6 }}
                    className="flex items-center justify-center gap-2 mb-6"
                >
                    <span className="text-accent-purple font-mono text-sm">&gt;&gt;</span>
                    <span className="text-base sm:text-xl md:text-2xl font-medium gradient-text font-display">
                        {typedText}
                    </span>
                    <span className="text-accent-purple font-mono text-xl animate-[blink_1s_infinite]">
                        |
                    </span>
                </motion.div>

                {/* Description */}
                <motion.p
                    initial={{ opacity: 0, y: 25, filter: "blur(8px)" }}
                    animate={{ opacity: 1, y: 0, filter: "blur(0px)" }}
                    transition={{ delay: 1.2, duration: 0.8 }}
                    className="text-muted text-sm sm:text-base md:text-lg max-w-2xl mx-auto mb-8 md:mb-10 leading-relaxed px-2 sm:px-0"
                >
                    {siteConfig.description}
                </motion.p>

                {/* CTAs */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 1.4, duration: 0.8, ease: [0.16, 1, 0.3, 1] }}
                    className="flex flex-col sm:flex-row items-center justify-center gap-3 sm:gap-4 mb-10 md:mb-16"
                >
                    <MagneticButton>
                        <a
                            href="#projects"
                            onClick={(e) => {
                                e.preventDefault();
                                const el = document.getElementById("projects");
                                if (el) {
                                    const top = el.getBoundingClientRect().top + window.scrollY - 20;
                                    window.scrollTo({ top, behavior: "smooth" });
                                }
                            }}
                            className="btn-primary"
                        >
                            <span>View My Work</span>
                            <svg
                                width="18"
                                height="18"
                                viewBox="0 0 24 24"
                                fill="none"
                                stroke="currentColor"
                                strokeWidth="2"
                            >
                                <path d="M7 17l9.2-9.2M17 17V7.8H7.8" />
                            </svg>
                        </a>
                    </MagneticButton>
                    <MagneticButton>
                        <a
                            href="#contact"
                            onClick={(e) => {
                                e.preventDefault();
                                const el = document.getElementById("contact");
                                if (el) {
                                    const top = el.getBoundingClientRect().top + window.scrollY - 20;
                                    window.scrollTo({ top, behavior: "smooth" });
                                }
                            }}
                            className="btn-outline"
                        >
                            <span>Let&apos;s Talk</span>
                        </a>
                    </MagneticButton>
                    <MagneticButton>
                        <a
                            href="/cv.pdf"
                            download
                            className="inline-flex items-center gap-2 px-6 py-3 text-sm font-medium rounded-full border border-white/[0.08] bg-white/[0.03] text-muted hover:text-foreground hover:bg-white/[0.06] hover:border-white/[0.15] transition-all duration-300"
                        >
                            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                                <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                                <polyline points="7 10 12 15 17 10" />
                                <line x1="12" y1="15" x2="12" y2="3" />
                            </svg>
                            <span>Download CV</span>
                        </a>
                    </MagneticButton>
                </motion.div>

                {/* Stats */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: 1.6, duration: 0.8 }}
                    className="flex items-center justify-center gap-4 sm:gap-8 md:gap-16 pb-10 md:pb-20"
                >
                    {siteConfig.stats.map((stat, i) => (
                        <div key={stat.label} className="flex items-center gap-4 sm:gap-8 md:gap-16">
                            <StatCounter value={stat.value} label={stat.label} />
                            {i < siteConfig.stats.length - 1 && (
                                <div className="w-px h-12 bg-white/[0.08]" />
                            )}
                        </div>
                    ))}
                </motion.div>
            </div>

            {/* Scroll Indicator */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 2.2, duration: 0.8 }}
                className="absolute bottom-6 left-1/2 -translate-x-1/2 flex flex-col items-center gap-1.5"
            >
                <span className="text-[10px] text-white/30 tracking-[0.25em] uppercase font-medium">Scroll</span>
                <motion.div
                    animate={{ y: [0, 6, 0] }}
                    transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                    className="w-5 h-8 rounded-full border border-white/[0.1] flex items-start justify-center pt-1.5"
                >
                    <motion.div
                        animate={{ opacity: [0.8, 0.2, 0.8], y: [0, 10, 0] }}
                        transition={{ duration: 2, repeat: Infinity, ease: "easeInOut" }}
                        className="w-0.5 h-1.5 rounded-full bg-white/40"
                    />
                </motion.div>
            </motion.div>
        </section>
    );
}
