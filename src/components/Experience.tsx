"use client";

import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import { experiences, type Experience as ExperienceType } from "@/data/portfolio";

const typeColors: Record<string, string> = {
    fulltime: "bg-accent-purple/20 text-accent-purple",
    freelance: "bg-accent-cyan/20 text-accent-cyan",
    contract: "bg-accent-pink/20 text-accent-pink",
    leadership: "bg-emerald-500/20 text-emerald-400",
};

const typeLabels: Record<string, string> = {
    fulltime: "Full-time",
    freelance: "Freelance",
    contract: "Contract",
    leadership: "Leadership",
};

function formatDate(d: string): string {
    const parts = d.split("-");
    if (parts.length < 2) return d;
    const [y, m] = parts;
    const months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    const monthIndex = parseInt(m, 10) - 1;
    return `${months[monthIndex] ?? m} ${y}`;
}

function ExperienceCard({ exp, index }: { exp: ExperienceType; index: number }) {
    const ref = useRef(null);
    const isInView = useInView(ref, { once: true, margin: "-60px" });

    return (
        <motion.div
            ref={ref}
            initial={{ opacity: 0, x: index % 2 === 0 ? -30 : 30 }}
            animate={isInView ? { opacity: 1, x: 0 } : {}}
            transition={{ duration: 0.6, delay: index * 0.1 }}
            className="relative pl-8 md:pl-12 pb-10 last:pb-0 group"
        >
            {/* Timeline line */}
            <div className="absolute left-0 md:left-3 top-2 bottom-0 w-px bg-gradient-to-b from-accent-purple/40 via-accent-cyan/20 to-transparent" />

            {/* Timeline dot */}
            <div className="absolute left-[-4px] md:left-[8px] top-2 w-[9px] h-[9px] rounded-full bg-accent-purple ring-4 ring-background group-hover:ring-accent-purple/20 transition-all duration-300">
                <div className="absolute inset-0 rounded-full bg-accent-purple animate-[badge-pulse_2s_ease-in-out_infinite]" />
            </div>

            {/* Card */}
            <div className="rounded-xl border border-white/[0.06] bg-white/[0.02] p-5 hover:bg-white/[0.04] hover:border-accent-purple/20 transition-all duration-300">
                {/* Header */}
                <div className="flex flex-wrap items-start justify-between gap-2 mb-3">
                    <div>
                        <h3 className="text-lg font-display font-semibold text-foreground">
                            {exp.role}
                        </h3>
                        <p className="text-accent-purple font-medium text-sm">
                            {exp.company}
                        </p>
                    </div>
                    <div className="flex items-center gap-2 flex-wrap">
                        <span className={`text-xs px-2.5 py-1 rounded-full font-medium ${typeColors[exp.type]}`}>
                            {typeLabels[exp.type]}
                        </span>
                    </div>
                </div>

                {/* Meta */}
                <div className="flex flex-wrap gap-x-4 gap-y-1 text-xs text-muted mb-3">
                    <span>{formatDate(exp.startDate)} — {exp.endDate ? formatDate(exp.endDate) : "Present"}</span>
                    <span>{exp.location}</span>
                </div>

                {/* Description */}
                <p className="text-sm text-muted mb-3 leading-relaxed">{exp.description}</p>

                {/* Highlights */}
                <ul className="space-y-1 mb-3">
                    {exp.highlights.map((h) => (
                        <li key={h} className="flex items-start gap-2 text-sm text-muted">
                            <span className="text-accent-purple mt-1.5 shrink-0">
                                <svg aria-hidden="true" focusable="false" width="8" height="8" viewBox="0 0 8 8" fill="currentColor">
                                    <circle cx="4" cy="4" r="3" />
                                </svg>
                            </span>
                            {h}
                        </li>
                    ))}
                </ul>

                {/* Tech tags */}
                {exp.tech.length > 0 && (
                    <div className="flex flex-wrap gap-1.5">
                        {exp.tech.map((t) => (
                            <span
                                key={t}
                                className="text-[11px] px-2 py-0.5 rounded-md bg-white/[0.05] text-muted border border-white/[0.06]"
                            >
                                {t}
                            </span>
                        ))}
                    </div>
                )}
            </div>
        </motion.div>
    );
}

export default function Experience() {
    const ref = useRef(null);
    const isInView = useInView(ref, { once: true, margin: "-100px" });

    return (
        <section id="experience" className="relative py-20 md:py-40 scroll-mt-20 overflow-hidden" ref={ref}>
            <div className="gradient-orb gradient-orb-cyan w-[400px] h-[400px] -top-20 -right-40" />
            <div className="gradient-orb gradient-orb-purple w-[300px] h-[300px] bottom-40 -left-20" style={{ animationDelay: "3s" }} />

            <div className="max-w-4xl mx-auto px-4 sm:px-6">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                    transition={{ duration: 0.6 }}
                    className="mb-10 md:mb-16"
                >
                    <span className="section-tag">&lt;experience&gt;</span>
                    <h2 className="section-title">
                        Work <span className="gradient-text">Experience</span>
                    </h2>
                    <div className="section-line" />
                </motion.div>

                {/* Timeline */}
                <div className="relative">
                    {experiences.map((exp, i) => (
                        <ExperienceCard key={exp.id} exp={exp} index={i} />
                    ))}
                </div>
            </div>
        </section>
    );
}
