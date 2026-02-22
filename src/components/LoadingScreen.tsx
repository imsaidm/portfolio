"use client";

import { useState, useEffect, useRef } from "react";
import { motion, AnimatePresence } from "framer-motion";

/**
 * LoadingScreen — waits for ALL real resources before dismissing:
 *   1. document.fonts.ready  (Google Fonts via next/font)
 *   2. window load event     (all scripts, stylesheets, etc.)
 *   3. Minimum 1.8s display  (so it doesn't flash)
 *
 * Progress bar reflects actual readiness instead of random increments.
 */
export default function LoadingScreen() {
    const [loading, setLoading] = useState(true);
    const [progress, setProgress] = useState(0);
    const readyFlags = useRef({ fonts: false, windowLoad: false, minTime: false });

    useEffect(() => {
        // Prevent scrolling during loading
        document.body.style.overflow = "hidden";

        let progressInterval: NodeJS.Timeout;
        let dismissed = false;

        const tryDismiss = () => {
            const f = readyFlags.current;
            if (f.fonts && f.windowLoad && f.minTime && !dismissed) {
                dismissed = true;
                // Smoothly finish progress
                setProgress(100);
                // Give the progress bar time to fill, then dismiss
                setTimeout(() => {
                    setLoading(false);
                    document.body.style.overflow = "";
                }, 400);
            }
        };

        // ── 1. Fonts ──
        document.fonts.ready.then(() => {
            readyFlags.current.fonts = true;
            setProgress((p) => Math.max(p, 40));
            tryDismiss();
        });

        // ── 2. Window load event (all scripts, stylesheets, sub-resources) ──
        const onLoad = () => {
            readyFlags.current.windowLoad = true;
            setProgress((p) => Math.max(p, 75));
            tryDismiss();
        };

        if (document.readyState === "complete") {
            onLoad();
        } else {
            window.addEventListener("load", onLoad);
        }

        // ── 3. Minimum display time ──
        const minTimer = setTimeout(() => {
            readyFlags.current.minTime = true;
            setProgress((p) => Math.max(p, 90));
            tryDismiss();
        }, 1800);

        // ── Animated progress (smooth increments tied to elapsed time) ──
        const startTime = performance.now();
        progressInterval = setInterval(() => {
            if (dismissed) return;
            const elapsed = performance.now() - startTime;
            const f = readyFlags.current;

            // Base progress from time (ease-out curve, caps at 85%)
            let base = Math.min(85, (elapsed / 2500) * 85);
            // Boost when individual tasks complete
            if (f.fonts) base = Math.max(base, 40);
            if (f.windowLoad) base = Math.max(base, 70);
            if (f.minTime) base = Math.max(base, 88);
            if (f.fonts && f.windowLoad) base = Math.max(base, 92);

            setProgress((p) => Math.max(p, Math.floor(base)));
        }, 60);

        return () => {
            clearInterval(progressInterval);
            clearTimeout(minTimer);
            window.removeEventListener("load", onLoad);
            document.body.style.overflow = "";
        };
    }, []);

    return (
        <AnimatePresence>
            {loading && (
                <motion.div
                    exit={{ opacity: 0, scale: 1.02 }}
                    transition={{ duration: 0.7, ease: [0.16, 1, 0.3, 1] }}
                    className="fixed inset-0 z-[9999] bg-[#050505] flex flex-col items-center justify-center"
                >
                    {/* Animated Logo */}
                    <motion.div
                        initial={{ scale: 0.5, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        transition={{ duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                        className="relative mb-12"
                    >
                        {/* Outer ring — progress-driven arc */}
                        <svg width="100" height="100" viewBox="0 0 100 100">
                            {/* Background ring */}
                            <circle
                                cx="50" cy="50" r="45"
                                fill="none"
                                stroke="rgba(255,255,255,0.05)"
                                strokeWidth="2"
                            />
                            {/* Progress arc */}
                            <motion.circle
                                cx="50" cy="50" r="45"
                                fill="none"
                                stroke="url(#grad-ring)"
                                strokeWidth="2"
                                strokeLinecap="round"
                                strokeDasharray="283"
                                strokeDashoffset={283 - (Math.min(progress, 100) / 100) * 283}
                                transform="rotate(-90, 50, 50)"
                                style={{ transition: "stroke-dashoffset 0.3s ease-out" }}
                            />
                            {/* Spinning glow overlay for animation feel */}
                            <motion.circle
                                cx="50" cy="50" r="45"
                                fill="none"
                                stroke="url(#grad-ring)"
                                strokeWidth="1"
                                strokeLinecap="round"
                                strokeDasharray="30 253"
                                transform="rotate(-90, 50, 50)"
                                style={{ opacity: 0.4 }}
                                animate={{ rotate: [0, 360] }}
                                transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                            />
                            <defs>
                                <linearGradient id="grad-ring" x1="0%" y1="0%" x2="100%" y2="100%">
                                    <stop offset="0%" stopColor="#00f0ff" />
                                    <stop offset="50%" stopColor="#a855f7" />
                                    <stop offset="100%" stopColor="#ec4899" />
                                </linearGradient>
                            </defs>
                        </svg>

                        {/* Center text */}
                        <div className="absolute inset-0 flex items-center justify-center">
                            <span className="font-mono text-xl font-bold">
                                <span className="text-accent-purple">&lt;</span>
                                <span className="text-foreground">SM</span>
                                <span className="text-accent-purple">/&gt;</span>
                            </span>
                        </div>
                    </motion.div>

                    {/* Progress bar */}
                    <motion.div
                        initial={{ opacity: 0, width: 0 }}
                        animate={{ opacity: 1, width: 220 }}
                        transition={{ delay: 0.2, duration: 0.5, ease: [0.16, 1, 0.3, 1] }}
                        className="h-[2px] bg-white/10 rounded-full overflow-hidden"
                    >
                        <div
                            className="h-full rounded-full"
                            style={{
                                width: `${Math.min(progress, 100)}%`,
                                background: "linear-gradient(90deg, #00f0ff, #a855f7, #ec4899)",
                                transition: "width 0.3s ease-out",
                            }}
                        />
                    </motion.div>

                    {/* Percentage */}
                    <motion.p
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 0.6 }}
                        transition={{ delay: 0.4 }}
                        className="mt-4 font-mono text-xs text-muted tracking-widest"
                    >
                        {Math.min(Math.floor(progress), 100)}%
                    </motion.p>

                    {/* Status text */}
                    <motion.p
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 0.35 }}
                        transition={{ delay: 0.6 }}
                        className="mt-2 font-mono text-[10px] text-muted tracking-widest uppercase"
                    >
                        {progress < 40
                            ? "Loading fonts..."
                            : progress < 75
                                ? "Preparing assets..."
                                : progress < 100
                                    ? "Almost ready..."
                                    : "Launching..."}
                    </motion.p>

                    {/* Background gradient orbs */}
                    <div className="absolute inset-0 overflow-hidden pointer-events-none">
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ duration: 1 }}
                            className="absolute top-1/4 left-1/4 w-96 h-96 bg-accent-purple/10 rounded-full blur-[120px]"
                            style={{ animation: "pulse 3s ease-in-out infinite" }}
                        />
                        <motion.div
                            initial={{ opacity: 0 }}
                            animate={{ opacity: 1 }}
                            transition={{ duration: 1, delay: 0.5 }}
                            className="absolute bottom-1/4 right-1/4 w-96 h-96 bg-accent-cyan/10 rounded-full blur-[120px]"
                            style={{ animation: "pulse 3s ease-in-out infinite 1.5s" }}
                        />
                    </div>
                </motion.div>
            )}
        </AnimatePresence>
    );
}
