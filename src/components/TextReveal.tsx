"use client";

import { ReactNode, useRef } from "react";
import { motion, useInView } from "framer-motion";

interface TextRevealProps {
    children: ReactNode;
    className?: string;
    delay?: number;
    once?: boolean;
}

export default function TextReveal({ children, className = "", delay = 0, once = true }: TextRevealProps) {
    const ref = useRef<HTMLSpanElement>(null);
    const isInView = useInView(ref, { once, margin: "-50px" });

    if (typeof children !== "string") {
        return (
            <motion.span
                ref={ref}
                initial={{ opacity: 0, y: 30, filter: "blur(8px)" }}
                animate={isInView ? { opacity: 1, y: 0, filter: "blur(0px)" } : {}}
                transition={{ duration: 0.6, delay, ease: [0.16, 1, 0.3, 1] }}
                className={`inline-block ${className}`}
            >
                {children}
            </motion.span>
        );
    }

    const words = children.split(" ");
    return (
        <span ref={ref} className={className}>
            {words.map((word, i) => (
                <span key={i} className="inline-block overflow-hidden mr-[0.25em]">
                    <motion.span
                        initial={{ y: "100%", opacity: 0 }}
                        animate={isInView ? { y: "0%", opacity: 1 } : {}}
                        transition={{
                            duration: 0.5,
                            delay: delay + i * 0.04,
                            ease: [0.16, 1, 0.3, 1],
                        }}
                        className="inline-block"
                    >
                        {word}
                    </motion.span>
                </span>
            ))}
        </span>
    );
}
