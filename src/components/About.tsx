"use client";

import { motion, useInView } from "framer-motion";
import { useRef } from "react";

const stats = [
    { value: "5+", label: "Years Experience" },
    { value: "50+", label: "Projects Delivered" },
    { value: "20+", label: "Technologies" },
    { value: "∞", label: "Cups of Coffee" },
];

const highlights = [
    {
        icon: (
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                <path d="M12 2L2 7l10 5 10-5-10-5z" /><path d="M2 17l10 5 10-5" /><path d="M2 12l10 5 10-5" />
            </svg>
        ),
        title: "Builds Everything",
        desc: "Web apps, mobile, games, bots, AI — if it involves code, I can make it.",
    },
    {
        icon: (
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                <circle cx="12" cy="12" r="10" /><path d="M12 6v6l4 2" />
            </svg>
        ),
        title: "Design + Engineering",
        desc: "Pixel-perfect UI fused with rock-solid architecture.",
    },
    {
        icon: (
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z" />
                <polyline points="7.5 4.21 12 6.81 16.5 4.21" /><polyline points="7.5 19.79 7.5 14.6 3 12" />
                <polyline points="21 12 16.5 14.6 16.5 19.79" /><polyline points="3.27 6.96 12 12.01 20.73 6.96" />
                <line x1="12" y1="22.08" x2="12" y2="12" />
            </svg>
        ),
        title: "Always Learning",
        desc: "New tech, new challenge — I adapt and master it fast.",
    },
];

export default function About() {
    const ref = useRef(null);
    const isInView = useInView(ref, { once: true, margin: "-100px" });

    return (
        <section id="about" className="relative py-20 md:py-40 scroll-mt-20 overflow-hidden" ref={ref}>
            {/* Gradient Orbs */}
            <div className="gradient-orb gradient-orb-purple w-[500px] h-[500px] -top-40 -left-40" />
            <div className="gradient-orb gradient-orb-cyan w-[300px] h-[300px] bottom-20 right-0" style={{ animationDelay: '4s' }} />

            <div className="max-w-7xl mx-auto px-4 sm:px-6">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                    transition={{ duration: 0.6 }}
                    className="mb-10 md:mb-16"
                >
                    <span className="section-tag">&lt;about&gt;</span>
                    <h2 className="section-title">
                        About <span className="gradient-text">Me</span>
                    </h2>
                    <div className="section-line" />
                </motion.div>

                <div className="grid lg:grid-cols-5 gap-12 lg:gap-16">
                    {/* Left: Text Content (3 cols) */}
                    <motion.div
                        initial={{ opacity: 0, x: -40 }}
                        animate={isInView ? { opacity: 1, x: 0 } : {}}
                        transition={{ duration: 0.8, delay: 0.2 }}
                        className="lg:col-span-3"
                    >
                        <h3 className="text-2xl md:text-3xl font-display font-semibold mb-6">
                            A tech enthusiast who{" "}
                            <span className="gradient-text">builds everything.</span>
                        </h3>
                        <p className="text-muted leading-relaxed mb-4">
                            I&apos;m a multidisciplinary developer and designer who believes in
                            the power of technology to transform ideas into reality. My
                            journey in tech has taken me through the entire spectrum — from
                            crafting beautiful user interfaces to architecting complex backend
                            systems, from building AI-powered solutions to developing immersive
                            games.
                        </p>
                        <p className="text-muted leading-relaxed mb-8">
                            I don&apos;t just write code — I engineer experiences. Whether it&apos;s
                            a sleek web application, an intelligent automation system, or an
                            interactive game, I approach every project with the same obsession
                            for quality and attention to detail.
                        </p>

                        {/* Highlight Cards */}
                        <div className="space-y-4">
                            {highlights.map((h, i) => (
                                <motion.div
                                    key={h.title}
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                                    transition={{ delay: 0.6 + i * 0.1 }}
                                    className="flex gap-4 p-4 rounded-xl border border-white/[0.06] bg-white/[0.02] hover:bg-white/[0.04] hover:border-accent-purple/20 transition-all duration-300 group"
                                >
                                    <div className="shrink-0 w-10 h-10 rounded-lg bg-accent-purple/10 flex items-center justify-center text-accent-purple group-hover:bg-accent-purple/20 transition-colors">
                                        {h.icon}
                                    </div>
                                    <div>
                                        <h4 className="font-semibold text-foreground mb-0.5">
                                            {h.title}
                                        </h4>
                                        <p className="text-sm text-muted">{h.desc}</p>
                                    </div>
                                </motion.div>
                            ))}
                        </div>
                    </motion.div>

                    {/* Right: Stats + Code Block (2 cols) */}
                    <motion.div
                        initial={{ opacity: 0, x: 40 }}
                        animate={isInView ? { opacity: 1, x: 0 } : {}}
                        transition={{ duration: 0.8, delay: 0.4 }}
                        className="lg:col-span-2 flex flex-col gap-6"
                    >
                        {/* Stats Grid */}
                        <div className="grid grid-cols-2 gap-4">
                            {stats.map((stat, i) => (
                                <motion.div
                                    key={stat.label}
                                    initial={{ opacity: 0, scale: 0.9 }}
                                    animate={isInView ? { opacity: 1, scale: 1 } : {}}
                                    transition={{ delay: 0.5 + i * 0.1 }}
                                    className="relative p-5 rounded-xl border border-white/[0.06] bg-white/[0.02] text-center group hover:border-accent-purple/20 hover:bg-white/[0.04] transition-all duration-300"
                                >
                                    <div className="text-2xl md:text-3xl font-display font-bold gradient-text mb-1">
                                        {stat.value}
                                    </div>
                                    <div className="text-xs text-muted uppercase tracking-wider">
                                        {stat.label}
                                    </div>
                                </motion.div>
                            ))}
                        </div>

                        {/* Code Terminal Card */}
                        <motion.div
                            initial={{ opacity: 0, y: 20 }}
                            animate={isInView ? { opacity: 1, y: 0 } : {}}
                            transition={{ delay: 0.8 }}
                            className="flex-1 rounded-xl border border-white/[0.08] bg-[rgba(10,10,15,0.8)] overflow-hidden"
                        >
                            {/* Terminal Header */}
                            <div className="flex items-center gap-2 px-4 py-3 border-b border-white/[0.06]">
                                <div className="w-3 h-3 rounded-full bg-red-500/80" />
                                <div className="w-3 h-3 rounded-full bg-yellow-500/80" />
                                <div className="w-3 h-3 rounded-full bg-green-500/80" />
                                <span className="ml-2 text-xs text-muted font-mono">about.ts</span>
                            </div>
                            {/* Code Content */}
                            <div className="p-4 font-mono text-sm leading-relaxed">
                                <div><span className="text-accent-purple">const</span> <span className="text-accent-cyan">developer</span> = {'{'}</div>
                                <div className="pl-4"><span className="text-accent-pink">name</span>: <span className="text-emerald-400">&quot;Said Mustaqim&quot;</span>,</div>
                                <div className="pl-4"><span className="text-accent-pink">role</span>: <span className="text-emerald-400">&quot;Tech Polymath&quot;</span>,</div>
                                <div className="pl-4"><span className="text-accent-pink">canDo</span>: <span className="text-emerald-400">&quot;literally everything&quot;</span>,</div>
                                <div className="pl-4"><span className="text-accent-pink">domains</span>: [</div>
                                <div className="pl-8"><span className="text-emerald-400">&quot;Full-Stack&quot;</span>,</div>
                                <div className="pl-8"><span className="text-emerald-400">&quot;AI / ML&quot;</span>,</div>
                                <div className="pl-8"><span className="text-emerald-400">&quot;Game Dev&quot;</span>,</div>
                                <div className="pl-8"><span className="text-emerald-400">&quot;Automation&quot;</span>,</div>
                                <div className="pl-8"><span className="text-emerald-400">&quot;Design&quot;</span></div>
                                <div className="pl-4">],</div>
                                <div className="pl-4"><span className="text-accent-pink">motto</span>: <span className="text-emerald-400">&quot;If it exists, I can build it&quot;</span></div>
                                <div>{'}'};</div>
                            </div>
                        </motion.div>
                    </motion.div>
                </div>
            </div>
        </section>
    );
}
