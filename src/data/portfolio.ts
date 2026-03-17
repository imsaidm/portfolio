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

export interface Experience {
  id: string;
  role: string;
  company: string;
  companyUrl?: string;
  type: "fulltime" | "freelance" | "contract" | "leadership";
  startDate: string;
  endDate?: string;
  location: string;
  description: string;
  highlights: string[];
  tech: string[];
}

export interface Education {
  id: string;
  institution: string;
  degree: string;
  field: string;
  startYear: number;
  endYear?: number;
  description?: string;
}

export type CertIcon = "shield" | "lock" | "code";

export interface Certification {
  id: string;
  name: string;
  issuer: string;
  icon: CertIcon;
}

export const siteConfig = {
  name: "Said Mustaqim",
  title: "Builder of Things That Shouldn't Exist Yet",
  description:
    "I've shipped 50+ products since age 16 — from AI automation pipelines for US companies to multiplayer RPGs with real-time combat. If it runs on code, I've probably built it.",
  social: {
    github: "https://github.com/imsaidm",
    linkedin: "https://www.linkedin.com/in/abdullahsaidmustaqim/",
    instagram: "https://instagram.com/imsaidm",
    tiktok: "https://tiktok.com/@imsaidm",
  },
  stats: [
    { label: "Projects Shipped", value: 50 },
    { label: "Tech Mastered", value: 20 },
    { label: "Years Building", value: 6 },
  ],
};

export const skills: Skill[] = [
  {
    category: "Frontend",
    icon: "code",
    description: "Interfaces that feel fast and look sharp",
    items: ["React", "Next.js", "Vue", "TypeScript", "Tailwind CSS", "Three.js", "GSAP", "Framer Motion"],
  },
  {
    category: "Backend",
    icon: "server",
    description: "APIs and systems that handle real traffic",
    items: ["Node.js", "Python", "Go", "PostgreSQL", "MongoDB", "Redis", "GraphQL", "REST API"],
  },
  {
    category: "AI & ML",
    icon: "brain",
    description: "LLMs, pipelines, and models in production",
    items: ["TensorFlow", "PyTorch", "LLM Integration", "NLP", "Computer Vision", "LangChain", "OpenAI API"],
  },
  {
    category: "UI/UX Design",
    icon: "palette",
    description: "Research-driven design, not guesswork",
    items: ["Figma", "Prototyping", "Design Systems", "Motion Design", "User Research", "Wireframing"],
  },
  {
    category: "Game Dev",
    icon: "gamepad",
    description: "From game engine to pixel art — solo",
    items: ["Unity", "C#", "Godot", "WebGL", "Game Design", "Physics Engine", "Canvas API"],
  },
  {
    category: "DevOps & Cloud",
    icon: "cloud",
    description: "Docker, CI/CD, and infra I manage myself",
    items: ["Docker", "AWS", "CI/CD", "Linux", "Cloudflare", "Nginx", "GitHub Actions", "VPS"],
  },
];

export const projects: Project[] = [
  {
    id: "epic-rpg",
    title: "Epic RPG Online",
    description:
      "Browser MMORPG with real-time Socket.io combat, 6 dungeons, 18+ monsters, crafting, and PvP duels. Built the entire game engine, server-authoritative logic, and pixel art UI solo.",
    longDescription:
      "Complete browser-based MMORPG featuring real-time multiplayer via Socket.io, turn-based combat against 18+ monsters, 6 dungeons with boss fights, crafting system, PvP dueling, and a full pixel art UI.",
    category: ["game", "web"],
    tags: ["Game", "Multiplayer", "Full-Stack"],
    tech: ["Node.js", "Express", "Socket.io", "SQLite", "HTML5", "CSS3", "JavaScript"],
    image: undefined,
    githubUrl: "https://github.com/imsaidm/epic-rpg-online",
    featured: true,
  },
  {
    id: "topupcuk",
    title: "TopupCuk",
    description:
      "Live e-commerce platform processing real payments via Tripay. Automated QRIS generation, instant email delivery, and a checkout flow that converts. Currently serving real users.",
    longDescription:
      "Full-featured e-commerce platform for digital goods with dynamic payment processing, email-based delivery, and a premium user experience.",
    category: ["web", "automation"],
    tags: ["E-Commerce", "Payment", "Full-Stack"],
    tech: ["Next.js", "Tailwind CSS", "Tripay API", "Resend", "Node.js"],
    image: undefined,
    liveUrl: "https://topupcuk.com",
    featured: true,
  },
  {
    id: "promovideohub",
    title: "PromoVideoHub",
    description:
      "Feed it a product brief, get a polished promo video. AI selects stock footage, composes scenes, adds transitions, and renders — zero manual editing. Built for Upwork clients.",
    longDescription:
      "End-to-end video production pipeline with AI-driven content generation, automated rendering, and cloud deployment.",
    category: ["web", "ai"],
    tags: ["AI", "Full-Stack", "Video"],
    tech: ["Next.js", "Python", "FFmpeg", "Docker", "Pexels API"],
    image: undefined,
    githubUrl: "https://github.com/imsaidm/promovideohub",
    featured: true,
  },
  {
    id: "openclaw",
    title: "OpenClaw AI Assistant",
    description:
      "Self-hosted AI assistant on personal infra, controlled via Telegram. Multi-user, custom personality, full command system — powered by Claude API. My daily driver.",
    longDescription:
      "A customizable AI chatbot deployed on personal infrastructure with Telegram as the primary interface, supporting multiple concurrent users.",
    category: ["ai", "automation"],
    tags: ["AI", "Bot", "Telegram"],
    tech: ["Node.js", "Claude API", "Telegram API", "Docker"],
    image: undefined,
    githubUrl: "https://github.com/imsaidm/openclaw",
    featured: true,
  },
  {
    id: "jobboard",
    title: "Job Board Platform",
    description:
      "Full-stack job marketplace: real-time search, smart filtering, applicant tracking, and employer dashboards. React frontend, Node.js API, PostgreSQL — production-grade architecture.",
    longDescription:
      "Full-stack job marketplace connecting employers and job seekers with intelligent matching and streamlined application workflows.",
    category: ["web"],
    tags: ["Full-Stack", "Platform", "CRUD"],
    tech: ["React", "Node.js", "PostgreSQL", "REST API", "Tailwind CSS"],
    image: undefined,
    githubUrl: "https://github.com/imsaidm/job-board",
    featured: true,
  },
  {
    id: "event-platform",
    title: "Event Management Platform",
    description:
      "End-to-end event platform: create events, sell tickets via Stripe, manage attendees, and track performance with live analytics.",
    longDescription:
      "Enterprise-grade event platform handling the full lifecycle from creation to post-event analytics.",
    category: ["web"],
    tags: ["Platform", "Full-Stack", "Dashboard"],
    tech: ["Next.js", "TypeScript", "PostgreSQL", "Stripe", "Tailwind CSS"],
    image: undefined,
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
    image: undefined,
    githubUrl: "https://github.com/imsaidm/cheatmc",
    featured: false,
  },
  {
    id: "trading-engine",
    title: "Algorithmic Trading Engine",
    description:
      "Quant trading engine that hit 7/7 performance KPIs. Grid-search optimized strategies, backtesting on historical data, and real-time signal generation for crypto markets.",
    longDescription:
      "Rule-based trading system optimized through grid search parameter tuning with comprehensive backtesting on historical data.",
    category: ["ai", "automation"],
    tags: ["Trading", "AI", "Quant"],
    tech: ["Python", "QuantConnect", "Pandas", "NumPy"],
    image: undefined,
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
    image: undefined,
    featured: false,
  },
  {
    id: "guidedgrowth",
    title: "GuidedGrowth Pipeline",
    description:
      "Drop a meeting recording, get structured action items in Asana. LLM-powered pipeline that summarizes, extracts tasks, and routes them — fully automated.",
    longDescription:
      "Automated workflow connecting meeting recordings to actionable tasks through AI-powered summarization and routing.",
    category: ["ai", "automation"],
    tags: ["AI", "Automation", "Pipeline"],
    tech: ["Python", "OpenAI", "Asana API", "GitHub Actions"],
    image: undefined,
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
    image: undefined,
    featured: false,
  },
];

export const experiences: Experience[] = [
  {
    id: "jtrip",
    role: "Director of Information Technology",
    company: "J-Trip",
    type: "fulltime",
    startDate: "2026-02",
    location: "Surabaya",
    description: "Leading IT strategy, infrastructure, and digital transformation for a growing travel tech company.",
    highlights: [
      "Own the technology roadmap across all business units — from infrastructure to product",
      "Drive architecture decisions and set engineering standards for the dev team",
      "Deploy AI automation that cuts manual operational work across departments",
    ],
    tech: ["Next.js", "Node.js", "PostgreSQL", "Docker", "AWS"],
  },
  {
    id: "fearless",
    role: "AI Workflow Automation Engineer",
    company: "The Fearless Life",
    type: "contract",
    startDate: "2026-02",
    location: "North America (Remote)",
    description: "Designing and building AI-powered automation pipelines for a US-based coaching and productivity company.",
    highlights: [
      "Architect AI pipelines that connect LLM APIs to real business workflows end-to-end",
      "Build systems that auto-generate content and extract intelligence from meetings",
      "Cut 60% of manual operational work — measurable impact, not just automation for automation's sake",
    ],
    tech: ["Python", "LangChain", "OpenAI API", "GitHub Actions", "Docker"],
  },
  {
    id: "quant",
    role: "Software Engineer Project Lead",
    company: "Quant Waru",
    type: "fulltime",
    startDate: "2025-10",
    location: "Surabaya",
    description: "Leading development of quantitative trading systems and algorithmic strategies for crypto markets.",
    highlights: [
      "Architect backtesting framework + real-time signal engine from scratch",
      "Hit 7/7 KPI targets on strategy performance — every single metric",
      "Build data pipelines powering market analysis and risk decisions",
    ],
    tech: ["Python", "QuantConnect", "Pandas", "NumPy", "TypeScript"],
  },
  {
    id: "upwork",
    role: "Full-Stack Developer",
    company: "Upwork",
    type: "freelance",
    startDate: "2026-01",
    location: "International Clients",
    description: "Delivering full-stack solutions and AI-driven automation for global clients on the world's largest freelance platform.",
    highlights: [
      "Build Node.js backends and Next.js frontends for diverse client needs",
      "Create AI video generation pipelines using FFmpeg and Python",
      "Maintain top-rated freelancer status with consistent 5-star reviews",
    ],
    tech: ["Node.js", "Next.js", "Python", "FFmpeg", "Docker"],
  },
  {
    id: "freelance",
    role: "Freelance Full-Stack Developer",
    company: "Self Employed",
    type: "freelance",
    startDate: "2020-01",
    location: "Surabaya",
    description: "Building web apps, AI systems, games, and automation tools for clients across Indonesia and internationally.",
    highlights: [
      "Shipped 50+ production projects: web apps, mobile, AI systems, games, trading bots",
      "Built e-commerce platforms, SaaS products, and trading systems that handle real money",
      "Started at 16, went pro immediately — no gap between learning and earning",
    ],
    tech: ["React", "Next.js", "Node.js", "Python", "Go", "PostgreSQL", "Docker"],
  },
  {
    id: "annora",
    role: "Mobile Developer Intern",
    company: "PT. Annora Multi Intech",
    type: "fulltime",
    startDate: "2024-08",
    endDate: "2024-09",
    location: "Surabaya",
    description: "Developed mobile application features and contributed to production codebases during a focused internship.",
    highlights: [
      "Implemented new mobile app features in production environment",
      "Collaborated with senior developers on code reviews and architecture",
    ],
    tech: ["Mobile Development", "REST API"],
  },
  {
    id: "chess",
    role: "Steering Committee & Head of Events",
    company: "UKM Catur Universitas Surabaya",
    type: "leadership",
    startDate: "2022-09",
    endDate: "2024-05",
    location: "Surabaya",
    description: "Organized and led university-level rapid chess competitions for two consecutive years.",
    highlights: [
      "Led all event operations for UBAYA Rapid Chess Competition 2023",
      "Promoted to Steering Committee for the 2024 edition",
      "Coordinated logistics, secured sponsorships, and managed 100+ participants",
    ],
    tech: [],
  },
];

export const educations: Education[] = [
  {
    id: "ubaya",
    institution: "Universitas Surabaya (UBAYA)",
    degree: "Bachelor of Science",
    field: "Information Technology",
    startYear: 2021,
    endYear: 2026,
    description: "Specializing in Network & Cyber Security. Led chess club events, shipped freelance projects throughout.",
  },
  {
    id: "purwadhika",
    institution: "Purwadhika Digital Technology School",
    degree: "Certificate",
    field: "Fullstack Web Development",
    startYear: 2025,
    endYear: 2025,
    description: "Intensive full-stack bootcamp: React, Node.js, cloud deployment. Formalized skills I'd been using professionally for years.",
  },
  {
    id: "smk",
    institution: "SMK Madinatul Quran",
    degree: "Vocational Diploma",
    field: "Computer Software Engineering",
    startYear: 2018,
    endYear: 2021,
    description: "Where it all started. Learned software engineering fundamentals, landed first paying clients before graduation.",
  },
];

export const certifications: Certification[] = [
  {
    id: "comptia",
    name: "CompTIA Security+",
    issuer: "CompTIA",
    icon: "shield",
  },
  {
    id: "google-cyber",
    name: "Google Cybersecurity Specialization",
    issuer: "Google",
    icon: "lock",
  },
  {
    id: "purwadhika-cert",
    name: "Fullstack Web Development",
    issuer: "Purwadhika",
    icon: "code",
  },
];

export const typingTexts = [
  "Director IT @ 22",
  "AI Engineer (US Remote)",
  "50+ Projects Shipped",
  "Full-Stack Since 16",
  "Game Dev & Chess Nerd",
  "Security+ Certified",
];
