"use client";

import { useRef } from "react";
import { motion, useInView } from "framer-motion";
import { educations, certifications, type CertIcon } from "@/data/portfolio";
import type { ReactNode } from "react";

const icons: Record<CertIcon, ReactNode> = {
    shield: (
        <svg aria-hidden="true" focusable="false" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
            <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
            <path d="m9 12 2 2 4-4" />
        </svg>
    ),
    lock: (
        <svg aria-hidden="true" focusable="false" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2" />
            <path d="M7 11V7a5 5 0 0 1 10 0v4" />
        </svg>
    ),
    code: (
        <svg aria-hidden="true" focusable="false" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
            <polyline points="16 18 22 12 16 6" />
            <polyline points="8 6 2 12 8 18" />
        </svg>
    ),
};

export default function Education() {
    const ref = useRef(null);
    const isInView = useInView(ref, { once: true, margin: "-100px" });

    return (
        <section id="education" className="relative py-16 md:py-28 scroll-mt-20 overflow-hidden" ref={ref}>
            <div className="max-w-7xl mx-auto px-4 sm:px-6">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                    transition={{ duration: 0.6 }}
                    className="mb-10 md:mb-14"
                >
                    <span className="section-tag">&lt;credentials&gt;</span>
                    <h2 className="section-title">
                        Education & <span className="gradient-text">Certifications</span>
                    </h2>
                    <div className="section-line" />
                </motion.div>

                {/* Education Grid */}
                <div className="grid md:grid-cols-3 gap-4 mb-10">
                    {educations.map((edu, i) => (
                        <motion.div
                            key={edu.id}
                            initial={{ opacity: 0, y: 20 }}
                            animate={isInView ? { opacity: 1, y: 0 } : {}}
                            transition={{ delay: 0.2 + i * 0.1 }}
                            className="rounded-xl border border-white/[0.06] bg-white/[0.02] p-5 hover:bg-white/[0.04] hover:border-accent-purple/20 transition-all duration-300 group"
                        >
                            {/* Graduation icon */}
                            <div className="w-10 h-10 rounded-lg bg-accent-purple/10 flex items-center justify-center text-accent-purple mb-4 group-hover:bg-accent-purple/20 transition-colors">
                                <svg aria-hidden="true" focusable="false" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5" strokeLinecap="round" strokeLinejoin="round">
                                    <path d="M22 10v6M2 10l10-5 10 5-10 5z" />
                                    <path d="M6 12v5c0 2 6 3 6 3s6-1 6-3v-5" />
                                </svg>
                            </div>

                            <h3 className="font-display font-semibold text-foreground mb-1">
                                {edu.institution}
                            </h3>
                            <p className="text-sm text-accent-purple font-medium mb-1">
                                {edu.degree} — {edu.field}
                            </p>
                            <p className="text-xs text-muted mb-3">
                                {edu.startYear} — {edu.endYear ?? "Present"}
                            </p>
                            {edu.description && (
                                <p className="text-sm text-muted leading-relaxed">
                                    {edu.description}
                                </p>
                            )}
                        </motion.div>
                    ))}
                </div>

                {/* Certifications Row */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                    transition={{ delay: 0.5 }}
                >
                    <h3 className="text-sm font-mono text-accent-cyan mb-4 tracking-wider uppercase">
                        Certifications
                    </h3>
                    <div className="flex flex-wrap gap-3">
                        {certifications.map((cert, i) => (
                            <motion.div
                                key={cert.id}
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={isInView ? { opacity: 1, scale: 1 } : {}}
                                transition={{ delay: 0.6 + i * 0.1 }}
                                className="flex items-center gap-3 rounded-full border border-white/[0.08] bg-white/[0.03] px-4 py-2.5 hover:border-accent-purple/25 hover:bg-white/[0.05] transition-all duration-300"
                            >
                                <div className="w-8 h-8 rounded-full bg-accent-purple/15 flex items-center justify-center text-accent-purple shrink-0">
                                    {icons[cert.icon]}
                                </div>
                                <div>
                                    <p className="text-sm font-semibold text-foreground leading-tight">
                                        {cert.name}
                                    </p>
                                    <p className="text-xs text-muted">{cert.issuer}</p>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                </motion.div>
            </div>
        </section>
    );
}
