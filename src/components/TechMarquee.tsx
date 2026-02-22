"use client";

import { techIconMap } from "@/data/techIcons";

const techItems = [
    "React", "Next.js", "TypeScript", "Node.js", "Python", "Tailwind CSS",
    "Three.js", "Framer Motion", "MongoDB", "PostgreSQL", "Docker", "AWS",
    "TensorFlow", "PyTorch", "Unity", "Godot", "Redis", "GraphQL",
    "Vue", "Go", "Cloudflare", "Linux", "GSAP", "Figma",
];

function TechPill({ name, accentClass }: { name: string; accentClass: string }) {
    const tech = techIconMap[name];
    const Icon = tech?.icon;
    const color = tech?.color ?? "#a855f7";

    return (
        <span
            className={`inline-flex items-center gap-2.5 px-5 py-2.5 rounded-full border border-white/[0.06] bg-white/[0.02] text-sm text-muted font-medium whitespace-nowrap hover:text-foreground hover:bg-white/[0.05] transition-all duration-300 cursor-default group ${accentClass}`}
        >
            {Icon ? (
                <span
                    className="text-[1.1rem] transition-all duration-300 group-hover:scale-125 group-hover:drop-shadow-[0_0_6px_currentColor]"
                    style={{ color }}
                >
                    <Icon />
                </span>
            ) : (
                <span className="w-2 h-2 rounded-full bg-accent-purple/60" />
            )}
            {name}
        </span>
    );
}

export default function TechMarquee() {
    return (
        <section className="relative py-16 overflow-hidden">
            {/* Fade edges */}
            <div className="absolute left-0 top-0 bottom-0 w-32 bg-gradient-to-r from-[#050505] to-transparent z-10" />
            <div className="absolute right-0 top-0 bottom-0 w-32 bg-gradient-to-l from-[#050505] to-transparent z-10" />

            {/* Row 1 — scrolls left */}
            <div className="flex mb-4 marquee-row">
                <div className="flex shrink-0 animate-marquee gap-4 pr-4">
                    {techItems.map((t, i) => (
                        <TechPill key={`a-${i}`} name={t} accentClass="hover:border-accent-purple/30" />
                    ))}
                </div>
                <div className="flex shrink-0 animate-marquee gap-4 pr-4" aria-hidden>
                    {techItems.map((t, i) => (
                        <TechPill key={`b-${i}`} name={t} accentClass="hover:border-accent-purple/30" />
                    ))}
                </div>
            </div>

            {/* Row 2 — scrolls right */}
            <div className="flex marquee-row">
                <div className="flex shrink-0 animate-marquee-reverse gap-4 pr-4">
                    {[...techItems].reverse().map((t, i) => (
                        <TechPill key={`c-${i}`} name={t} accentClass="hover:border-accent-cyan/30" />
                    ))}
                </div>
                <div className="flex shrink-0 animate-marquee-reverse gap-4 pr-4" aria-hidden>
                    {[...techItems].reverse().map((t, i) => (
                        <TechPill key={`d-${i}`} name={t} accentClass="hover:border-accent-cyan/30" />
                    ))}
                </div>
            </div>
        </section>
    );
}
