export interface Project {
  id: string;
  title: string;
  description: string;
  longDescription: string;
  category: string[];
  tags: string[];
  tech: string[];
  image?: string;
  liveUrl?: string;
  githubUrl?: string;
  featured: boolean;
}

export interface Skill {
  category: string;
  icon: string;
  description: string;
  items: string[];
}

export const siteConfig = {
  name: "Said Mustaqim",
  title: "Tech Enthusiast",
  description:
    "I build things that live on the internet. From pixel-perfect interfaces to intelligent systems — I turn complex problems into elegant solutions.",
  social: {
    github: "https://github.com/imsaidm",
    linkedin: "https://www.linkedin.com/in/abdullahsaidmustaqim/",
    instagram: "https://instagram.com/imsaidm",
    tiktok: "https://tiktok.com/@imsaidm",
  },
  stats: [
    { label: "Projects Built", value: 50 },
    { label: "Technologies", value: 20 },
    { label: "Years Coding", value: 5 },
  ],
};

export const skills: Skill[] = [
  {
    category: "Frontend",
    icon: "code",
    description: "Crafting responsive, beautiful interfaces",
    items: ["React", "Next.js", "Vue", "TypeScript", "Tailwind CSS", "Three.js", "GSAP", "Framer Motion"],
  },
  {
    category: "Backend",
    icon: "server",
    description: "Building robust, scalable systems",
    items: ["Node.js", "Python", "Go", "PostgreSQL", "MongoDB", "Redis", "GraphQL", "REST API"],
  },
  {
    category: "AI & ML",
    icon: "brain",
    description: "Intelligent solutions & automation",
    items: ["TensorFlow", "PyTorch", "LLM Integration", "NLP", "Computer Vision", "LangChain", "OpenAI API"],
  },
  {
    category: "UI/UX Design",
    icon: "palette",
    description: "Human-centered design thinking",
    items: ["Figma", "Prototyping", "Design Systems", "Motion Design", "User Research", "Wireframing"],
  },
  {
    category: "Game Dev",
    icon: "gamepad",
    description: "Immersive interactive experiences",
    items: ["Unity", "C#", "Godot", "WebGL", "Game Design", "Physics Engine", "Canvas API"],
  },
  {
    category: "DevOps & Cloud",
    icon: "cloud",
    description: "Shipping fast, scaling smart",
    items: ["Docker", "AWS", "CI/CD", "Linux", "Cloudflare", "Nginx", "GitHub Actions", "VPS"],
  },
];

export const projects: Project[] = [
  {
    id: "epic-rpg",
    title: "Epic RPG Online",
    description:
      "Web-based multiplayer RPG game with real-time combat, dungeons, crafting, and PvP duels. Pixel art aesthetic with full game mechanics including leveling, inventory, and boss fights.",
    longDescription:
      "Complete browser-based MMORPG featuring real-time multiplayer via Socket.io, turn-based combat against 18+ monsters, 6 dungeons with boss fights, crafting system, PvP dueling, and a full pixel art UI.",
    category: ["game", "web"],
    tags: ["Game", "Multiplayer", "Full-Stack"],
    tech: ["Node.js", "Express", "Socket.io", "SQLite", "HTML5", "CSS3", "JavaScript"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=Epic+RPG",
    githubUrl: "https://github.com/imsaidm/epic-rpg-online",
    featured: true,
  },
  {
    id: "topupcuk",
    title: "TopupCuk",
    description:
      "A sleek digital top-up marketplace with integrated payment gateway, automated QRIS generation, and instant delivery system for digital products.",
    longDescription:
      "Full-featured e-commerce platform for digital goods with dynamic payment processing, email-based delivery, and a premium user experience.",
    category: ["web", "automation"],
    tags: ["E-Commerce", "Payment", "Full-Stack"],
    tech: ["Next.js", "Tailwind CSS", "Tripay API", "Resend", "Node.js"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=TopupCuk",
    liveUrl: "https://topupcuk.com",
    featured: true,
  },
  {
    id: "promovideohub",
    title: "PromoVideoHub",
    description:
      "AI-powered promotional video generation platform. Automatically creates engaging marketing videos with intelligent scene composition and dynamic transitions.",
    longDescription:
      "End-to-end video production pipeline with AI-driven content generation, automated rendering, and cloud deployment.",
    category: ["web", "ai"],
    tags: ["AI", "Full-Stack", "Video"],
    tech: ["Next.js", "Python", "FFmpeg", "Docker", "Pexels API"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=PromoVideoHub",
    githubUrl: "https://github.com/imsaidm/promovideohub",
    featured: true,
  },
  {
    id: "openclaw",
    title: "OpenClaw AI Assistant",
    description:
      "Self-hosted AI assistant with Telegram integration. Multi-user chat bot powered by Claude API with configurable personality and command system.",
    longDescription:
      "A customizable AI chatbot deployed on personal infrastructure with Telegram as the primary interface, supporting multiple concurrent users.",
    category: ["ai", "automation"],
    tags: ["AI", "Bot", "Telegram"],
    tech: ["Node.js", "Claude API", "Telegram API", "Docker"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=OpenClaw+AI",
    githubUrl: "https://github.com/imsaidm/openclaw",
    featured: true,
  },
  {
    id: "jobboard",
    title: "Job Board Platform",
    description:
      "Modern job listing platform with advanced filtering, real-time search, and applicant tracking. Features responsive design and employer dashboards.",
    longDescription:
      "Full-stack job marketplace connecting employers and job seekers with intelligent matching and streamlined application workflows.",
    category: ["web"],
    tags: ["Full-Stack", "Platform", "CRUD"],
    tech: ["React", "Node.js", "PostgreSQL", "REST API", "Tailwind CSS"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=Job+Board",
    githubUrl: "https://github.com/imsaidm/job-board",
    featured: true,
  },
  {
    id: "event-platform",
    title: "Event Management Platform",
    description:
      "Comprehensive event management system with ticketing, scheduling, attendee management, and real-time analytics dashboard.",
    longDescription:
      "Enterprise-grade event platform handling the full lifecycle from creation to post-event analytics.",
    category: ["web"],
    tags: ["Platform", "Full-Stack", "Dashboard"],
    tech: ["Next.js", "TypeScript", "PostgreSQL", "Stripe", "Tailwind CSS"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=Event+Platform",
    githubUrl: "https://github.com/imsaidm/event-platform",
    featured: true,
  },
  {
    id: "cheatmc",
    title: "CheatMC",
    description:
      "Predictive gaming assistant with persistent learning. Features drag-and-drop player management, real-time pairing predictions, and adaptive AI.",
    longDescription:
      "Browser-based game prediction tool that learns from historical patterns to predict future pairings and outcomes.",
    category: ["game", "ai"],
    tags: ["Game", "AI", "Web"],
    tech: ["JavaScript", "Canvas API", "Machine Learning", "LocalStorage"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=CheatMC",
    githubUrl: "https://github.com/imsaidm/cheatmc",
    featured: false,
  },
  {
    id: "trading-engine",
    title: "Algorithmic Trading Engine",
    description:
      "Quantitative trading strategy engine achieving 7/7 KPIs. Technical analysis, backtesting framework, and automated signal generation for crypto markets.",
    longDescription:
      "Rule-based trading system optimized through grid search parameter tuning with comprehensive backtesting on historical data.",
    category: ["ai", "automation"],
    tags: ["Trading", "AI", "Quant"],
    tech: ["Python", "QuantConnect", "Pandas", "NumPy"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=Trading+Engine",
    featured: false,
  },
  {
    id: "solana-bot",
    title: "Solana Trading Bot",
    description:
      "Self-hosted trading and volume bot for Pump.fun on Solana. Wallet management, automated strategies, and secure Telegram-based control.",
    longDescription:
      "Chat-based trading interface for Solana DEX with automated volume generation and multi-wallet management.",
    category: ["automation", "web"],
    tags: ["Bot", "Blockchain", "Web3"],
    tech: ["Node.js", "Solana Web3.js", "Telegram API", "TypeScript"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=Solana+Bot",
    featured: false,
  },
  {
    id: "guidedgrowth",
    title: "GuidedGrowth Pipeline",
    description:
      "Intelligent meeting-to-action pipeline. Processes recordings, extracts insights with AI, and creates structured tasks in project management tools.",
    longDescription:
      "Automated workflow connecting meeting recordings to actionable tasks through AI-powered summarization and routing.",
    category: ["ai", "automation"],
    tags: ["AI", "Automation", "Pipeline"],
    tech: ["Python", "OpenAI", "Asana API", "GitHub Actions"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=GuidedGrowth",
    githubUrl: "https://github.com/imsaidm/guidedgrowth",
    featured: false,
  },
  {
    id: "cf-bypass",
    title: "Cloudflare Bypass Tool",
    description:
      "Advanced web security research tool demonstrating deep understanding of web security, HTTP protocols, and browser fingerprinting techniques.",
    longDescription:
      "Security research project exploring Cloudflare protection mechanisms and browser automation techniques.",
    category: ["automation"],
    tags: ["Security", "Research", "Automation"],
    tech: ["Python", "Selenium", "HTTP", "Browser Automation"],
    image: "https://placehold.co/800x450/1a1a2e/a855f7?text=CF+Bypass",
    featured: false,
  },
];

export const typingTexts = [
  "Tech Enthusiast",
  "Full-Stack Developer",
  "AI Engineer",
  "Game Developer",
  "UI/UX Designer",
  "Automation Builder",
  "Problem Solver",
];
