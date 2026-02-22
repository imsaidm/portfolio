import {
    SiReact, SiNextdotjs, SiTypescript, SiNodedotjs, SiPython, SiTailwindcss,
    SiThreedotjs, SiFramer, SiMongodb, SiPostgresql, SiDocker, SiAmazonwebservices,
    SiTensorflow, SiPytorch, SiUnity, SiGodotengine, SiRedis, SiGraphql,
    SiVuedotjs, SiGo, SiCloudflare, SiLinux, SiGreensock, SiFigma,
    SiJavascript, SiGithubactions, SiNginx, SiStripe, SiSolana,
    SiOpenai, SiAsana, SiSelenium, SiElectron,
    SiNumpy, SiPandas, SiSharp,
} from "react-icons/si";
import { IconType } from "react-icons";

export interface TechIcon {
    icon: IconType;
    color: string;
}

export const techIconMap: Record<string, TechIcon> = {
    // Frontend
    "React": { icon: SiReact, color: "#61DAFB" },
    "Next.js": { icon: SiNextdotjs, color: "#ffffff" },
    "TypeScript": { icon: SiTypescript, color: "#3178C6" },
    "Vue": { icon: SiVuedotjs, color: "#4FC08D" },
    "Tailwind CSS": { icon: SiTailwindcss, color: "#06B6D4" },
    "Three.js": { icon: SiThreedotjs, color: "#ffffff" },
    "Framer Motion": { icon: SiFramer, color: "#0055FF" },
    "GSAP": { icon: SiGreensock, color: "#88CE02" },
    "JavaScript": { icon: SiJavascript, color: "#F7DF1E" },

    // Backend
    "Node.js": { icon: SiNodedotjs, color: "#5FA04E" },
    "Python": { icon: SiPython, color: "#3776AB" },
    "Go": { icon: SiGo, color: "#00ADD8" },
    "PostgreSQL": { icon: SiPostgresql, color: "#4169E1" },
    "MongoDB": { icon: SiMongodb, color: "#47A248" },
    "Redis": { icon: SiRedis, color: "#DC382D" },
    "GraphQL": { icon: SiGraphql, color: "#E10098" },
    "REST API": { icon: SiNodedotjs, color: "#5FA04E" },

    // AI & ML
    "TensorFlow": { icon: SiTensorflow, color: "#FF6F00" },
    "PyTorch": { icon: SiPytorch, color: "#EE4C2C" },
    "OpenAI API": { icon: SiOpenai, color: "#412991" },
    "OpenAI": { icon: SiOpenai, color: "#412991" },
    "NumPy": { icon: SiNumpy, color: "#013243" },
    "Pandas": { icon: SiPandas, color: "#150458" },

    // Design
    "Figma": { icon: SiFigma, color: "#F24E1E" },

    // Game Dev
    "Unity": { icon: SiUnity, color: "#ffffff" },
    "Godot": { icon: SiGodotengine, color: "#478CBF" },
    "C#": { icon: SiSharp, color: "#512BD4" },

    // DevOps & Cloud
    "Docker": { icon: SiDocker, color: "#2496ED" },
    "AWS": { icon: SiAmazonwebservices, color: "#FF9900" },
    "Cloudflare": { icon: SiCloudflare, color: "#F38020" },
    "Linux": { icon: SiLinux, color: "#FCC624" },
    "Nginx": { icon: SiNginx, color: "#009639" },
    "GitHub Actions": { icon: SiGithubactions, color: "#2088FF" },

    // Other
    "Stripe": { icon: SiStripe, color: "#635BFF" },
    "Solana Web3.js": { icon: SiSolana, color: "#9945FF" },
    "Selenium": { icon: SiSelenium, color: "#43B02A" },
    "Electron": { icon: SiElectron, color: "#47848F" },
    "Asana API": { icon: SiAsana, color: "#F06A6A" },

    // APIs (use related icons)
    "Tripay API": { icon: SiStripe, color: "#635BFF" },
    "Claude API": { icon: SiOpenai, color: "#D97757" },
    "Telegram API": { icon: SiReact, color: "#26A5E4" },
    "Pexels API": { icon: SiReact, color: "#05A081" },
};

/** Helper: get icon component for a tech name, returns null if not found */
export function getTechIcon(name: string): TechIcon | null {
    return techIconMap[name] ?? null;
}
