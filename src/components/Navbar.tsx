"use client";

import { useState, useEffect, useRef, useCallback } from "react";
import { motion, AnimatePresence } from "framer-motion";

const navLinks = [
    { href: "#about", label: "About" },
    { href: "#skills", label: "Skills" },
    { href: "#projects", label: "Projects" },
    { href: "#contact", label: "Contact" },
];

export default function Navbar() {
    const [scrolled, setScrolled] = useState(false);
    const [mobileOpen, setMobileOpen] = useState(false);
    const [activeSection, setActiveSection] = useState("");

    // Refs for direct DOM manipulation (no re-renders)
    const progressBarRef = useRef<HTMLDivElement>(null);
    const cometRef = useRef<HTMLDivElement>(null);
    const rafRef = useRef<number>(0);
    const lastActiveSectionRef = useRef("");
    const lastScrolledRef = useRef(false);

    const updateScroll = useCallback(() => {
        const scrollY = window.scrollY;

        // Update scrolled state only when crossing threshold
        const isScrolled = scrollY > 50;
        if (isScrolled !== lastScrolledRef.current) {
            lastScrolledRef.current = isScrolled;
            setScrolled(isScrolled);
        }

        // Update scroll progress bar via DOM (no re-render)
        const totalHeight = document.documentElement.scrollHeight - window.innerHeight;
        const progress = totalHeight > 0 ? (scrollY / totalHeight) * 100 : 0;

        if (progressBarRef.current) {
            progressBarRef.current.style.width = `${progress}%`;
            progressBarRef.current.style.opacity = progress > 0 ? "1" : "0";
            progressBarRef.current.style.boxShadow = progress > 0
                ? "0 0 12px rgba(168, 85, 247, 0.6), 0 0 24px rgba(0, 240, 255, 0.4), 0 0 4px rgba(251,191,36,0.3)"
                : "none";
        }

        if (cometRef.current) {
            cometRef.current.style.left = `${progress}%`;
            cometRef.current.style.opacity = progress > 0 ? "1" : "0";
            cometRef.current.style.transform = progress > 0 ? "translateY(-50%) scale(1)" : "translateY(-50%) scale(0)";
        }

        // Detect active section
        const sections = navLinks.map((l) => l.href.slice(1));
        let found = "";
        for (const id of [...sections].reverse()) {
            const el = document.getElementById(id);
            if (el && el.getBoundingClientRect().top <= 200) {
                found = id;
                break;
            }
        }

        // Only update state if section actually changed
        if (found !== lastActiveSectionRef.current) {
            lastActiveSectionRef.current = found;
            setActiveSection(found);
        }

        rafRef.current = 0;
    }, []);

    useEffect(() => {
        const onScroll = () => {
            // Throttle with rAF — max once per frame
            if (rafRef.current) return;
            rafRef.current = requestAnimationFrame(updateScroll);
        };
        window.addEventListener("scroll", onScroll, { passive: true });
        // Run once on mount
        updateScroll();
        return () => {
            window.removeEventListener("scroll", onScroll);
            if (rafRef.current) cancelAnimationFrame(rafRef.current);
        };
    }, [updateScroll]);

    const handleClick = (href: string) => {
        setMobileOpen(false);
        const el = document.querySelector(href);
        if (el) {
            const offset = 20; // just enough to clear navbar
            const top = el.getBoundingClientRect().top + window.scrollY - offset;
            window.scrollTo({ top, behavior: "smooth" });
        }
    };

    return (
        <motion.nav
            initial={{ y: -100 }}
            animate={{ y: 0 }}
            transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
            className={`fixed top-0 left-0 right-0 z-50 transition-all duration-500 ${scrolled
                ? "bg-[rgba(5,5,5,0.8)] backdrop-blur-xl"
                : "bg-transparent"
                }`}
        >
            <div className="max-w-7xl mx-auto px-6 h-16 flex items-center justify-between">
                {/* Logo */}
                <a
                    href="#hero"
                    onClick={(e) => {
                        e.preventDefault();
                        window.scrollTo({ top: 0, behavior: "smooth" });
                    }}
                    className="font-mono text-lg font-bold tracking-tight group"
                >
                    <span className="text-accent-purple group-hover:text-accent-cyan transition-colors duration-300">
                        &lt;
                    </span>
                    <span className="text-foreground">SM</span>
                    <span className="text-accent-purple group-hover:text-accent-cyan transition-colors duration-300">
                        /&gt;
                    </span>
                </a>

                {/* Desktop Links */}
                <ul className="hidden md:flex items-center gap-2">
                    {navLinks.map((link) => (
                        <li key={link.href}>
                            <button
                                onClick={() => handleClick(link.href)}
                                className={`relative px-4 py-2 text-sm font-medium transition-colors duration-300 rounded-lg ${activeSection === link.href.slice(1)
                                    ? "text-accent-purple"
                                    : "text-muted hover:text-foreground"
                                    }`}
                            >
                                {link.label}
                                {activeSection === link.href.slice(1) && (
                                    <motion.div
                                        layoutId="nav-active"
                                        className="absolute inset-0 bg-white/[0.04] rounded-lg"
                                        transition={{ type: "spring", stiffness: 500, damping: 35, mass: 0.8 }}
                                    />
                                )}
                            </button>
                        </li>
                    ))}
                </ul>

                {/* Mobile Toggle */}
                <button
                    onClick={() => setMobileOpen(!mobileOpen)}
                    className="md:hidden w-10 h-10 flex flex-col items-center justify-center gap-1.5 relative z-50"
                    aria-label="Toggle menu"
                >
                    <motion.span
                        animate={mobileOpen ? { rotate: 45, y: 6 } : { rotate: 0, y: 0 }}
                        className="block w-5 h-[2px] bg-foreground origin-center"
                    />
                    <motion.span
                        animate={mobileOpen ? { opacity: 0, scaleX: 0 } : { opacity: 1, scaleX: 1 }}
                        className="block w-5 h-[2px] bg-foreground"
                    />
                    <motion.span
                        animate={mobileOpen ? { rotate: -45, y: -6 } : { rotate: 0, y: 0 }}
                        className="block w-5 h-[2px] bg-foreground origin-center"
                    />
                </button>
            </div>

            {/* Scroll Progress Bar with Code Comet */}
            <div className="absolute bottom-0 left-0 right-0 h-[3px] bg-transparent overflow-visible">
                {/* Progress line — ref-driven, no re-renders */}
                <div
                    ref={progressBarRef}
                    className="h-full rounded-r-full"
                    style={{
                        width: "0%",
                        opacity: 0,
                        background: "linear-gradient(90deg, #fbbf24, #a855f7, #00f0ff, #ec4899)",
                        transition: "opacity 0.2s",
                    }}
                />

                {/* ✨ Enhanced Comet element — ref-driven */}
                <div
                    ref={cometRef}
                    className="comet-container absolute top-1/2 pointer-events-none"
                    style={{
                        left: "0%",
                        opacity: 0,
                        transform: "translateY(-50%) scale(0)",
                        transition: "opacity 0.3s, transform 0.3s",
                    }}
                >
                    {/* === LAYER 1: Massive nebula aura === */}
                    <div
                        className="comet-nebula absolute rounded-full"
                        style={{
                            width: 90,
                            height: 90,
                            background: "radial-gradient(circle, rgba(0,240,255,0.15) 0%, rgba(168,85,247,0.06) 30%, rgba(251,191,36,0.03) 55%, transparent 70%)",
                        }}
                    />

                    {/* === LAYER 2: Outer energy ring === */}
                    <div
                        className="comet-ring-outer absolute rounded-full"
                        style={{
                            width: 48,
                            height: 48,
                            border: "1px solid rgba(0,240,255,0.15)",
                            background: "radial-gradient(circle, rgba(0,240,255,0.12) 0%, transparent 60%)",
                        }}
                    />

                    {/* === LAYER 3: Inner plasma ring === */}
                    <div
                        className="comet-ring-inner absolute rounded-full"
                        style={{
                            width: 28,
                            height: 28,
                            border: "1.5px solid rgba(168,85,247,0.2)",
                            background: "radial-gradient(circle, rgba(168,85,247,0.25) 0%, rgba(251,191,36,0.1) 50%, transparent 70%)",
                        }}
                    />

                    {/* === LAYER 4: Hot core with double glow === */}
                    <div
                        className="comet-core absolute rounded-full"
                        style={{
                            width: 14,
                            height: 14,
                            background: "radial-gradient(circle, rgba(255,255,255,0.9) 0%, rgba(0,240,255,0.6) 30%, rgba(168,85,247,0.3) 60%, transparent 100%)",
                            boxShadow: "0 0 6px #fff, 0 0 12px #00f0ff, 0 0 24px rgba(168,85,247,0.8), 0 0 40px rgba(251,191,36,0.3)",
                        }}
                    />
                    {/* Inner white-hot core */}
                    <div
                        className="comet-core-hot absolute rounded-full"
                        style={{
                            width: 5,
                            height: 5,
                            background: "#fff",
                            boxShadow: "0 0 4px #fff, 0 0 8px #00f0ff",
                        }}
                    />

                    {/* === LAYER 5: Rotating code symbol </> === */}
                    <div className="comet-symbol absolute flex items-center justify-center">
                        <span
                            className="text-[10px] font-mono font-black select-none"
                            style={{
                                color: "#fff",
                                textShadow: "0 0 6px #fff, 0 0 12px rgba(0,240,255,1), 0 0 24px rgba(168,85,247,0.8), 0 0 36px rgba(251,191,36,0.5), 0 0 48px rgba(236,72,153,0.3)",
                            }}
                        >
                            &lt;/&gt;
                        </span>
                    </div>

                    {/* === LAYER 6: Orbiting electrons (3) === */}
                    {[0, 1, 2].map((i) => (
                        <div
                            key={`orbit-${i}`}
                            className={`comet-orbit-${i} absolute`}
                            style={{ width: 0, height: 0, animationDelay: `${-i * 0.5}s` }}
                        >
                            <div
                                className="comet-electron absolute rounded-full"
                                style={{
                                    width: [3, 2.5, 2][i],
                                    height: [3, 2.5, 2][i],
                                    background: ["#00f0ff", "#a855f7", "#fbbf24"][i],
                                    boxShadow: `0 0 6px ${["#00f0ff", "#a855f7", "#fbbf24"][i]}`,
                                    left: [18, 22, 15][i],
                                    top: -1,
                                    animationDelay: `${i * 0.3}s`,
                                }}
                            />
                        </div>
                    ))}

                    {/* === LAYER 7: Trailing sparkle particles (10) === */}
                    {[0, 1, 2, 3, 4, 5, 6, 7, 8, 9].map((i) => (
                        <div
                            key={`spark-${i}`}
                            className={`comet-spark comet-spark-${i} absolute rounded-full`}
                            style={{
                                width: [2, 3.5, 2.5, 4, 2, 3, 1.5, 3, 2, 2.5][i],
                                height: [2, 3.5, 2.5, 4, 2, 3, 1.5, 3, 2, 2.5][i],
                                background: ["#fbbf24", "#00f0ff", "#a855f7", "#f472b6", "#34d399", "#818cf8", "#fff", "#ec4899", "#10b981", "#f59e0b"][i],
                                left: -6 - i * 6,
                                top: "50%",
                                boxShadow: `0 0 6px ${["#fbbf24", "#00f0ff", "#a855f7", "#f472b6", "#34d399", "#818cf8", "#fff", "#ec4899", "#10b981", "#f59e0b"][i]}`,
                            }}
                        />
                    ))}

                    {/* === LAYER 8: Primary comet tail (long, vivid) === */}
                    <div
                        className="absolute top-1/2 h-[3px] rounded-full"
                        style={{
                            right: 0,
                            width: 80,
                            transform: "translateX(-100%) translateY(-50%)",
                            background: "linear-gradient(90deg, transparent 0%, rgba(251,191,36,0.2) 15%, rgba(0,240,255,0.5) 40%, rgba(168,85,247,0.7) 70%, rgba(236,72,153,0.9) 100%)",
                        }}
                    />
                    {/* Secondary soft glow tail */}
                    <div
                        className="absolute top-1/2 h-[8px] rounded-full"
                        style={{
                            right: 0,
                            width: 60,
                            transform: "translateX(-100%) translateY(-50%)",
                            background: "linear-gradient(90deg, transparent, rgba(0,240,255,0.08), rgba(168,85,247,0.12), rgba(236,72,153,0.15))",
                            filter: "blur(3px)",
                        }}
                    />
                    {/* Tertiary wide ambient tail */}
                    <div
                        className="absolute top-1/2 h-[14px] rounded-full"
                        style={{
                            right: 0,
                            width: 40,
                            transform: "translateX(-100%) translateY(-50%)",
                            background: "linear-gradient(90deg, transparent, rgba(168,85,247,0.04), rgba(0,240,255,0.06))",
                            filter: "blur(6px)",
                        }}
                    />
                </div>
            </div>

            {/* Mobile Menu */}
            <AnimatePresence>
                {mobileOpen && (
                    <motion.div
                        initial={{ opacity: 0, height: 0 }}
                        animate={{ opacity: 1, height: "auto" }}
                        exit={{ opacity: 0, height: 0 }}
                        transition={{ duration: 0.3 }}
                        className="md:hidden bg-[rgba(5,5,5,0.95)] backdrop-blur-2xl border-t border-white/[0.06]"
                    >
                        <div className="px-6 py-6 flex flex-col gap-2">
                            {navLinks.map((link, i) => (
                                <motion.button
                                    key={link.href}
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    transition={{ delay: i * 0.05 }}
                                    onClick={() => handleClick(link.href)}
                                    className="text-left text-lg font-medium py-3 px-4 rounded-xl text-muted hover:text-foreground hover:bg-white/[0.04] transition-all"
                                >
                                    {link.label}
                                </motion.button>
                            ))}
                        </div>
                    </motion.div>
                )}
            </AnimatePresence>
        </motion.nav>
    );
}
