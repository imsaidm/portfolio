"use client";

import { motion, useInView } from "framer-motion";
import { useRef } from "react";
import { skills } from "@/data/portfolio";
import { techIconMap } from "@/data/techIcons";

const iconMap: Record<string, React.ReactNode> = {
    code: (
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <polyline points="16 18 22 12 16 6" /><polyline points="8 6 2 12 8 18" /><line x1="14" y1="4" x2="10" y2="20" />
        </svg>
    ),
    server: (
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <rect x="2" y="2" width="20" height="8" rx="2" /><rect x="2" y="14" width="20" height="8" rx="2" />
            <circle cx="6" cy="6" r="1" /><circle cx="6" cy="18" r="1" />
        </svg>
    ),
    brain: (
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M9.5 2A5.5 5.5 0 0 0 4 7.5c0 1.58.67 3 1.74 4.01L4 16l3.5-1.5A5.5 5.5 0 1 0 9.5 2z" />
            <path d="M14.5 2A5.5 5.5 0 0 1 20 7.5c0 1.58-.67 3-1.74 4.01L20 16l-3.5-1.5A5.5 5.5 0 1 1 14.5 2z" />
            <path d="M8 14s1.5 2 4 2 4-2 4-2" />
        </svg>
    ),
    palette: (
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M12 2C6.5 2 2 6.5 2 12s4.5 10 10 10c.926 0 1.648-.746 1.648-1.688 0-.437-.18-.835-.437-1.125-.29-.289-.438-.652-.438-1.125a1.64 1.64 0 0 1 1.668-1.668h1.996c3.051 0 5.555-2.503 5.555-5.555C21.965 6.012 17.461 2 12 2z" />
            <circle cx="7.5" cy="10.5" r="1.5" /><circle cx="10.5" cy="7" r="1.5" />
            <circle cx="14.5" cy="7" r="1.5" /><circle cx="17" cy="10.5" r="1.5" />
        </svg>
    ),
    gamepad: (
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <rect x="2" y="6" width="20" height="12" rx="4" /><path d="M8 12h4" /><path d="M10 10v4" />
            <circle cx="17" cy="10" r="1" /><circle cx="15" cy="14" r="1" />
        </svg>
    ),
    cloud: (
        <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
            <path d="M22 12h-4l-3 9L9 3l-3 9H2" />
        </svg>
    ),
};

function SkillTag({ item }: { item: string }) {
    const tech = techIconMap[item];
    const Icon = tech?.icon;
    const color = tech?.color;

    return (
        <span
            className="inline-flex items-center gap-1.5 px-2.5 py-1 text-xs font-medium rounded-lg bg-white/[0.04] border border-white/[0.06] text-muted hover:text-foreground hover:border-accent-purple/30 hover:bg-white/[0.08] hover:scale-105 hover:shadow-[0_0_12px_rgba(168,85,247,0.15)] transition-all duration-300 cursor-default group"
        >
            {Icon && (
                <span
                    className="text-[0.8rem] transition-all duration-300 group-hover:drop-shadow-[0_0_4px_currentColor]"
                    style={{ color }}
                >
                    <Icon />
                </span>
            )}
            {item}
        </span>
    );
}

export default function Skills() {
    const ref = useRef(null);
    const isInView = useInView(ref, { once: true, margin: "-100px" });

    return (
        <section id="skills" className="relative py-20 md:py-40 scroll-mt-20 overflow-hidden" ref={ref}>
            <div className="max-w-7xl mx-auto px-4 sm:px-6">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                    transition={{ duration: 0.6 }}
                    className="mb-16"
                >
                    <span className="section-tag">&lt;skills&gt;</span>
                    <h2 className="section-title">
                        My <span className="gradient-text">Arsenal</span>
                    </h2>
                    <div className="section-line" />
                </motion.div>

                {/* Skills Grid */}
                <div className="grid sm:grid-cols-2 lg:grid-cols-3 gap-6">
                    {skills.map((skill, i) => (
                        <motion.div
                            key={skill.category}
                            initial={{ opacity: 0, y: 40 }}
                            animate={isInView ? { opacity: 1, y: 0 } : {}}
                            transition={{ delay: i * 0.1, duration: 0.6, ease: [0.16, 1, 0.3, 1] }}
                            className="group relative p-6 rounded-2xl border border-white/[0.06] bg-white/[0.02] hover:bg-white/[0.04] hover:border-accent-purple/20 transition-all duration-500 overflow-hidden"
                        >
                            {/* Glow on hover */}
                            <div className="absolute inset-0 opacity-0 group-hover:opacity-100 transition-opacity duration-500 pointer-events-none">
                                <div className="absolute -inset-[100px] bg-accent-purple/5 blur-3xl" />
                            </div>

                            <div className="relative z-10">
                                {/* Icon */}
                                <div className="w-12 h-12 rounded-xl bg-gradient-to-br from-accent-purple/20 to-accent-pink/10 border border-accent-purple/20 flex items-center justify-center text-accent-purple mb-4 group-hover:scale-110 group-hover:shadow-[0_0_20px_rgba(168,85,247,0.3)] transition-all duration-500">
                                    {iconMap[skill.icon]}
                                </div>

                                <h3 className="text-lg font-display font-semibold mb-1">
                                    {skill.category}
                                </h3>
                                <p className="text-sm text-muted mb-4">{skill.description}</p>

                                {/* Tags with real icons */}
                                <div className="flex flex-wrap gap-2">
                                    {skill.items.map((item) => (
                                        <SkillTag key={item} item={item} />
                                    ))}
                                </div>
                            </div>
                        </motion.div>
                    ))}
                </div>
            </div>
        </section>
    );
}
