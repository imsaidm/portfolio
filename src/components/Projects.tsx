"use client";

import { motion, useInView, AnimatePresence } from "framer-motion";
import { useRef, useState, useCallback } from "react";
import { projects } from "@/data/portfolio";
import { techIconMap } from "@/data/techIcons";

const filters = [
    { key: "all", label: "All" },
    { key: "web", label: "Web App" },
    { key: "ai", label: "AI / ML" },
    { key: "game", label: "Game" },
    { key: "automation", label: "Automation" },
];

const hueMap: Record<string, number> = {
    topupcuk: 200,
    promovideohub: 280,
    openclaw: 180,
    jobboard: 30,
    "event-platform": 340,
    cheatmc: 140,
    "trading-engine": 310,
    "solana-bot": 40,
    guidedgrowth: 260,
    "cf-bypass": 60,
};

function ProjectTechIcons({ techs, hue }: { techs: string[]; hue: number }) {
    // Show up to 5 tech icons in a scattered arrangement
    const positions = [
        { x: "50%", y: "50%", size: 28, delay: 0 },
        { x: "25%", y: "35%", size: 22, delay: 0.1 },
        { x: "75%", y: "35%", size: 22, delay: 0.15 },
        { x: "30%", y: "68%", size: 18, delay: 0.2 },
        { x: "70%", y: "68%", size: 18, delay: 0.25 },
    ];

    return (
        <div className="absolute inset-0 flex items-center justify-center">
            {techs.slice(0, 5).map((t, i) => {
                const tech = techIconMap[t];
                const Icon = tech?.icon;
                const color = tech?.color ?? `hsl(${hue}, 70%, 60%)`;
                const pos = positions[i];

                if (!Icon) {
                    return (
                        <div
                            key={t}
                            className="absolute opacity-40 group-hover:opacity-70 transition-all duration-500"
                            style={{
                                left: pos.x,
                                top: pos.y,
                                transform: "translate(-50%, -50%)",
                                fontSize: pos.size,
                                color: `hsl(${hue}, 70%, 60%)`,
                            }}
                        >
                            <svg width={pos.size} height={pos.size} viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.5">
                                <polyline points="16 18 22 12 16 6" /><polyline points="8 6 2 12 8 18" />
                            </svg>
                        </div>
                    );
                }

                return (
                    <motion.div
                        key={t}
                        className="absolute group-hover:opacity-80 transition-all duration-500"
                        style={{
                            left: pos.x,
                            top: pos.y,
                            transform: "translate(-50%, -50%)",
                            fontSize: pos.size,
                            color,
                            opacity: i === 0 ? 0.6 : 0.35,
                            filter: `drop-shadow(0 0 8px ${color}40)`,
                        }}
                        initial={{ scale: 0, opacity: 0 }}
                        animate={{ scale: 1, opacity: i === 0 ? 0.6 : 0.35 }}
                        transition={{ delay: pos.delay, duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                    >
                        <Icon />
                    </motion.div>
                );
            })}
        </div>
    );
}

export default function Projects() {
    const ref = useRef(null);
    const isInView = useInView(ref, { once: true, margin: "-100px" });
    const [active, setActive] = useState("all");

    const filtered =
        active === "all"
            ? projects
            : projects.filter((p) => p.category.includes(active));

    const handleTilt = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
        const card = e.currentTarget;
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(800px) rotateY(${x * 10}deg) rotateX(${-y * 10}deg) scale3d(1.02, 1.02, 1.02)`;
    }, []);

    const resetTilt = useCallback((e: React.MouseEvent<HTMLDivElement>) => {
        e.currentTarget.style.transform = 'perspective(800px) rotateY(0deg) rotateX(0deg) scale3d(1, 1, 1)';
    }, []);

    return (
        <section id="projects" className="relative py-20 md:py-40 scroll-mt-20 overflow-hidden" ref={ref}>
            {/* Gradient Orbs */}
            <div className="gradient-orb gradient-orb-pink w-[400px] h-[400px] -top-20 -right-20" style={{ animationDelay: '2s' }} />

            <div className="max-w-7xl mx-auto px-4 sm:px-6">
                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: 30 }}
                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                    transition={{ duration: 0.6 }}
                    className="mb-12"
                >
                    <span className="section-tag">&lt;projects&gt;</span>
                    <h2 className="section-title">
                        Featured <span className="gradient-text">Work</span>
                    </h2>
                    <div className="section-line" />
                </motion.div>

                {/* Filters */}
                <motion.div
                    initial={{ opacity: 0, y: 20 }}
                    animate={isInView ? { opacity: 1, y: 0 } : {}}
                    transition={{ delay: 0.2, duration: 0.5 }}
                    className="flex flex-wrap gap-2 mb-12"
                >
                    {filters.map((f) => (
                        <button
                            key={f.key}
                            onClick={() => setActive(f.key)}
                            className={`relative px-5 py-2 text-sm font-medium rounded-full transition-all duration-300 ${active === f.key
                                ? "text-white"
                                : "text-muted hover:text-foreground border border-white/[0.08] hover:border-white/[0.15] bg-white/[0.02]"
                                }`}
                        >
                            {active === f.key && (
                                <motion.div
                                    layoutId="filter-bg"
                                    className="absolute inset-0 bg-gradient-to-r from-accent-purple to-accent-pink rounded-full"
                                    transition={{ type: "spring", stiffness: 400, damping: 30 }}
                                />
                            )}
                            <span className="relative z-10">{f.label}</span>
                        </button>
                    ))}
                </motion.div>

                {/* Grid */}
                <motion.div layout className="grid sm:grid-cols-2 lg:grid-cols-3 gap-4 sm:gap-6">
                    <AnimatePresence mode="popLayout">
                        {filtered.map((project) => {
                            const hue = hueMap[project.id] ?? 200;
                            return (
                                <motion.div
                                    key={project.id}
                                    layout
                                    initial={{ opacity: 0, scale: 0.9 }}
                                    animate={{ opacity: 1, scale: 1 }}
                                    exit={{ opacity: 0, scale: 0.9 }}
                                    transition={{ duration: 0.4, ease: [0.16, 1, 0.3, 1] }}
                                >
                                    <div
                                        className="tilt-card group relative rounded-2xl border border-white/[0.06] bg-white/[0.02] overflow-hidden hover:border-accent-purple/20 transition-all duration-300"
                                        onMouseMove={handleTilt}
                                        onMouseLeave={resetTilt}
                                        style={{ transformStyle: 'preserve-3d', transition: 'transform 0.2s ease-out' }}
                                    >
                                        {/* 3D Glare overlay */}
                                        <div className="tilt-glare" />

                                        {/* Image area with tech icons */}
                                        <div
                                            className="relative h-48 overflow-hidden"
                                            style={{
                                                background: `linear-gradient(135deg, hsl(${hue}, 60%, 15%), hsl(${hue + 40}, 40%, 8%))`,
                                            }}
                                        >
                                            {/* Project image if available */}
                                            {project.image && (
                                                <img
                                                    src={project.image}
                                                    alt={project.title}
                                                    className="absolute inset-0 w-full h-full object-cover rounded-t-2xl"
                                                    style={{ aspectRatio: '16/9' }}
                                                    loading="lazy"
                                                />
                                            )}

                                            {/* Decorative grid pattern */}
                                            <div
                                                className="absolute inset-0 opacity-[0.04]"
                                                style={{
                                                    backgroundImage: `radial-gradient(circle, hsl(${hue}, 70%, 60%) 1px, transparent 1px)`,
                                                    backgroundSize: "20px 20px",
                                                }}
                                            />

                                            {/* Tech stack icons */}
                                            <ProjectTechIcons techs={project.tech} hue={hue} />

                                            {/* Overlay on hover */}
                                            <div className="absolute inset-0 bg-black/60 opacity-0 group-hover:opacity-100 transition-all duration-400 flex items-center justify-center gap-3 z-10">
                                                {project.liveUrl && (
                                                    <a href={project.liveUrl} target="_blank" rel="noopener" className="w-10 h-10 rounded-full bg-white/10 border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all">
                                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                                            <path d="M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6" /><polyline points="15 3 21 3 21 9" /><line x1="10" y1="14" x2="21" y2="3" />
                                                        </svg>
                                                    </a>
                                                )}
                                                {project.githubUrl && (
                                                    <a href={project.githubUrl} target="_blank" rel="noopener" className="w-10 h-10 rounded-full bg-white/10 border border-white/20 flex items-center justify-center text-white hover:bg-white/20 transition-all">
                                                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                                                            <polyline points="16 18 22 12 16 6" /><polyline points="8 6 2 12 8 18" />
                                                        </svg>
                                                    </a>
                                                )}
                                            </div>

                                            {/* Featured badge */}
                                            {project.featured && (
                                                <div className="absolute top-3 right-3 px-2.5 py-1 text-[10px] font-semibold tracking-wider uppercase bg-accent-purple/80 backdrop-blur-sm text-white rounded-full z-10">
                                                    Featured
                                                </div>
                                            )}
                                        </div>

                                        {/* Info */}
                                        <div className="p-5">
                                            <div className="flex flex-wrap gap-1.5 mb-3">
                                                {project.tags.map((tag) => (
                                                    <span key={tag} className="px-2 py-0.5 text-[10px] font-semibold tracking-wide uppercase rounded-md bg-accent-purple/10 text-accent-purple border border-accent-purple/20">
                                                        {tag}
                                                    </span>
                                                ))}
                                            </div>
                                            <h3 className="text-lg font-display font-semibold mb-2 group-hover:text-accent-purple transition-colors duration-300">
                                                {project.title}
                                            </h3>
                                            <p className="text-sm text-muted leading-relaxed mb-4 line-clamp-3">
                                                {project.description}
                                            </p>
                                            <div className="flex flex-wrap gap-1.5">
                                                {project.tech.map((t) => {
                                                    const tech = techIconMap[t];
                                                    const Icon = tech?.icon;
                                                    const color = tech?.color;
                                                    return (
                                                        <span key={t} className="inline-flex items-center gap-1 text-[11px] font-mono text-muted/60 bg-white/[0.03] px-2 py-0.5 rounded hover:text-foreground hover:bg-white/[0.06] transition-all duration-200">
                                                            {Icon && (
                                                                <span style={{ color, fontSize: "0.7rem" }}>
                                                                    <Icon />
                                                                </span>
                                                            )}
                                                            {t}
                                                        </span>
                                                    );
                                                })}
                                            </div>
                                        </div>
                                    </div>
                                </motion.div>
                            );
                        })}
                    </AnimatePresence>
                </motion.div>
            </div>
        </section>
    );
}
