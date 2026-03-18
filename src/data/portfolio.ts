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
    image: "/thumbnails/epic-rpg.png",
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
    image: "/thumbnails/topupcuk.png",
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
    image: "/thumbnails/promovideohub.png",
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
    image: "/thumbnails/openclaw.png",
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
    image: "/thumbnails/jobboard.png",
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
    image: "/thumbnails/event-platform.png",
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
    image: "/thumbnails/cheatmc.png",
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
    image: "/thumbnails/trading-engine.png",
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
    image: "/thumbnails/solana-bot.png",
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
    image: "/thumbnails/guidedgrowth.png",
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
    image: "/thumbnails/cf-bypass.png",
    featured: false,
  },
  // ============ SHOWCASE PROJECTS ============
  {
    id: "animegen",
    title: "AnimeGen Studio",
    description: "AI-powered anime character generator using Stable Diffusion fine-tuned on 50K+ illustrations. Pose control, expression modifiers, and consistent style across generations.",
    longDescription: "End-to-end anime character generation pipeline leveraging fine-tuned diffusion models with LoRA adapters, ControlNet pose guidance, and a React-based editor.",
    category: ["ai"],
    tags: ["AI", "Generative Art", "Stable Diffusion"],
    tech: ["Python", "Stable Diffusion", "PyTorch", "React", "FastAPI", "ControlNet"],
    image: "/thumbnails/animegen.png",
    featured: false,
  },
  {
    id: "arfurniture",
    title: "AR Furniture Visualizer",
    description: "Point your phone at any room, drop in 3D furniture to-scale with real lighting. ARCore surface detection, PBR materials, and shadow casting — feels like it's actually there.",
    longDescription: "Mobile AR application for real-time furniture placement using ARCore plane detection, physically-based rendering, and occlusion handling.",
    category: ["web"],
    tags: ["AR", "Mobile", "3D"],
    tech: ["Kotlin", "ARCore", "Sceneform", "Blender", "Firebase"],
    image: "/thumbnails/arfurniture.png",
    featured: false,
  },
  {
    id: "artgen",
    title: "ArtGen Collective",
    description: "Collaborative AI art platform where users co-create with generative models. Style transfer, inpainting, outpainting, and a community gallery with upvote-driven curation.",
    longDescription: "Social generative art platform combining multiple AI models with collaborative editing tools, version history, and community-driven discovery.",
    category: ["ai", "web"],
    tags: ["AI", "Art", "Community"],
    tech: ["Next.js", "Python", "OpenAI API", "Stable Diffusion", "Supabase", "Tailwind CSS"],
    image: "/thumbnails/artgen.png",
    featured: false,
  },
  {
    id: "blockvote",
    title: "BlockVote DAO",
    description: "Decentralized voting with zero-knowledge proof identity verification. Voters prove eligibility without revealing identity — tamper-proof, auditable, and fully on-chain.",
    longDescription: "Blockchain-based governance platform implementing zk-SNARK identity proofs, quadratic voting mechanisms, and on-chain proposal lifecycle management.",
    category: ["web"],
    tags: ["Blockchain", "Web3", "ZK-Proofs"],
    tech: ["Solidity", "Hardhat", "React", "ethers.js", "Circom", "IPFS"],
    image: "/thumbnails/blockvote.png",
    featured: true,
  },
  {
    id: "botarmy",
    title: "BotArmy Orchestrator",
    description: "Multi-bot management platform controlling 200+ concurrent Telegram, Discord, and Slack bots from a single dashboard. Health monitoring, log aggregation, one-click deploy.",
    longDescription: "Centralized bot orchestration system with Docker-based deployment, real-time health monitoring, centralized logging, and a management dashboard.",
    category: ["automation", "web"],
    tags: ["Bot", "Automation", "DevOps"],
    tech: ["Node.js", "Docker", "Redis", "Grafana", "Loki", "React", "WebSocket"],
    image: "/thumbnails/botarmy.png",
    featured: false,
  },
  {
    id: "chatverse",
    title: "ChatVerse",
    description: "Real-time chat supporting 10K+ concurrent users with E2EE, message threading, file sharing, and AI smart replies. Sub-50ms message delivery.",
    longDescription: "Scalable real-time messaging platform with Signal Protocol E2EE, WebSocket delivery, Redis pub/sub for horizontal scaling, and LLM-powered reply suggestions.",
    category: ["web", "ai"],
    tags: ["Real-Time", "Chat", "E2EE"],
    tech: ["Next.js", "Socket.io", "Redis", "PostgreSQL", "Signal Protocol", "OpenAI API"],
    image: "/thumbnails/chatverse.png",
    featured: false,
  },
  {
    id: "cloudnotes",
    title: "CloudNotes",
    description: "Notion-inspired note-taking with real-time collaboration, block-based editor, nested pages, and offline-first sync. Supports Markdown, code blocks, and embedded media.",
    longDescription: "Block-based collaborative editor built on CRDTs for conflict-free real-time editing, with offline-first architecture using IndexedDB.",
    category: ["web"],
    tags: ["Productivity", "Collaboration", "Editor"],
    tech: ["React", "TypeScript", "Yjs", "Hocuspocus", "Supabase", "TipTap", "Tailwind CSS"],
    image: "/thumbnails/cloudnotes.png",
    featured: false,
  },
  {
    id: "codeforge",
    title: "CodeForge IDE",
    description: "Browser-based collaborative IDE with AI code completion, integrated terminal, Git GUI, and live preview. 20+ languages with LSP intellisense — zero local setup.",
    longDescription: "Cloud-hosted dev environment built on Monaco Editor with LSP integration, Docker sandboxed execution, and real-time pair programming via CRDT.",
    category: ["web", "ai"],
    tags: ["IDE", "AI", "Developer Tools"],
    tech: ["React", "Monaco Editor", "Node.js", "Docker", "WebSocket", "LSP", "OpenAI API"],
    image: "/thumbnails/codeforge.png",
    featured: true,
  },
  {
    id: "cryptodash",
    title: "CryptoDash Analytics",
    description: "Real-time crypto portfolio tracker with whale monitoring, on-chain analytics, and AI sentiment scores. 500+ tokens across 8 chains.",
    longDescription: "Multi-chain cryptocurrency analytics dashboard aggregating on-chain data, DEX activity, and social sentiment into actionable insights.",
    category: ["web"],
    tags: ["Crypto", "Analytics", "Dashboard"],
    tech: ["Next.js", "Python", "Web3.js", "PostgreSQL", "Chart.js", "Redis", "WebSocket"],
    image: "/thumbnails/cryptodash.png",
    featured: false,
  },
  {
    id: "cybershield",
    title: "CyberShield SIEM",
    description: "Lightweight SIEM ingesting syslog, Windows Events, and cloud audit trails. Real-time threat detection with YARA rules, automated incident response playbooks.",
    longDescription: "Security Information and Event Management system with log ingestion from 15+ sources, real-time correlation engine, and automated incident response.",
    category: ["automation"],
    tags: ["Security", "SIEM", "Threat Detection"],
    tech: ["Go", "Elasticsearch", "Kibana", "Python", "YARA", "Docker", "Kafka"],
    image: "/thumbnails/cybershield.png",
    featured: true,
  },
  {
    id: "datavis",
    title: "DataVis Pro",
    description: "Drag-and-drop data visualization builder. Connect any SQL database or CSV, build dashboards with 30+ chart types, share via embeddable links.",
    longDescription: "No-code analytics dashboard builder with direct database connections, NLP query generation, and 30+ chart types including heatmaps and geospatial plots.",
    category: ["web"],
    tags: ["Data Viz", "Dashboard", "Analytics"],
    tech: ["React", "D3.js", "Node.js", "PostgreSQL", "Apache ECharts", "Tailwind CSS"],
    image: "/thumbnails/datavis.png",
    featured: false,
  },
  {
    id: "devportfolio",
    title: "DevPortfolio Engine",
    description: "Open-source portfolio generator. Feed it your GitHub profile — auto-generates project cards, tech radar, contribution graph, and blog CMS.",
    longDescription: "Automated developer portfolio generator that pulls data from GitHub API, npm, and LinkedIn to create a customizable static site.",
    category: ["web", "automation"],
    tags: ["Open Source", "Portfolio", "Generator"],
    tech: ["Next.js", "TypeScript", "GitHub API", "MDX", "Tailwind CSS", "Vercel"],
    image: "/thumbnails/devportfolio.png",
    featured: false,
  },
  {
    id: "docscanner",
    title: "DocScanner AI",
    description: "Mobile document scanner with AI OCR, auto-cropping, perspective correction, and structured data extraction. Scans receipts, IDs, contracts — outputs searchable PDFs.",
    longDescription: "On-device document scanning combining OpenCV edge detection with Tesseract OCR and custom NER models for field extraction.",
    category: ["ai"],
    tags: ["Mobile", "OCR", "AI"],
    tech: ["React Native", "OpenCV", "Tesseract", "TensorFlow Lite", "Python", "FastAPI"],
    image: "/thumbnails/docscanner.png",
    featured: false,
  },
  {
    id: "droneview",
    title: "DroneView Command",
    description: "Drone fleet management with live video feeds, GPS tracking, automated flight paths, and no-fly zone enforcement. Controls up to 12 drones simultaneously.",
    longDescription: "Real-time drone fleet control platform with RTMP video streaming, MAVLink protocol integration, and automated mission planning.",
    category: ["web"],
    tags: ["IoT", "Drones", "Real-Time"],
    tech: ["React", "Node.js", "MAVLink", "WebRTC", "Mapbox", "PostgreSQL", "Redis"],
    image: "/thumbnails/droneview.png",
    featured: false,
  },
  {
    id: "dungeonai",
    title: "DungeonAI Master",
    description: "AI D&D dungeon master generating dynamic storylines, NPC dialogues, combat encounters, and loot tables in real-time. 100+ session context via vector memory.",
    longDescription: "Interactive AI dungeon master leveraging GPT-4 with RAG-based campaign memory, procedural encounter generation, and multi-player sessions.",
    category: ["game", "ai"],
    tags: ["Game", "AI", "RPG"],
    tech: ["Next.js", "OpenAI API", "Pinecone", "LangChain", "Socket.io", "TypeScript"],
    image: "/thumbnails/dungeonai.png",
    featured: false,
  },
  {
    id: "ecotrack",
    title: "EcoTrack Carbon Monitor",
    description: "Carbon footprint tracker for individuals and companies. Scans receipts, calculates emissions via EPA datasets, gamifies reduction with badges and leaderboards.",
    longDescription: "Carbon monitoring platform integrating receipt OCR, EPA emission databases, and behavioral nudge algorithms.",
    category: ["web"],
    tags: ["Sustainability", "Data", "Gamification"],
    tech: ["Next.js", "Python", "PostgreSQL", "Chart.js", "Tesseract", "Tailwind CSS"],
    image: "/thumbnails/ecotrack.png",
    featured: false,
  },
  {
    id: "fittrack",
    title: "FitTrack Pro",
    description: "AI fitness coach with personalized workout plans. Tracks exercises via phone camera pose estimation, counts reps, and corrects form in real-time.",
    longDescription: "Fitness tracking with MediaPipe pose estimation for real-time form analysis, progressive overload algorithm, and social challenges.",
    category: ["ai"],
    tags: ["Fitness", "AI", "Mobile"],
    tech: ["React Native", "MediaPipe", "TensorFlow Lite", "Node.js", "MongoDB", "Firebase"],
    image: "/thumbnails/fittrack.png",
    featured: false,
  },
  {
    id: "gamelobby",
    title: "GameLobby Matchmaker",
    description: "Multiplayer game lobby with ELO matchmaking, party queues, anti-cheat, and spectator mode. 5K concurrent players, sub-100ms match latency.",
    longDescription: "Scalable matchmaking service with ELO/Glicko-2 rating, skill-based queue balancing, and WebSocket lobby sync.",
    category: ["game", "web"],
    tags: ["Game", "Multiplayer", "Matchmaking"],
    tech: ["Go", "Redis", "WebSocket", "PostgreSQL", "Docker", "React"],
    image: "/thumbnails/gamelobby.png",
    featured: false,
  },
  {
    id: "healthpulse",
    title: "HealthPulse Dashboard",
    description: "Hospital patient monitoring aggregating vitals from IoT wearables in real-time. Anomaly detection triggers nurse alerts within 3 seconds. HIPAA-compliant.",
    longDescription: "Clinical monitoring system ingesting real-time vitals from BLE wearables with ML anomaly detection and HL7 FHIR compliance.",
    category: ["web"],
    tags: ["Healthcare", "IoT", "Real-Time"],
    tech: ["React", "Node.js", "InfluxDB", "MQTT", "TensorFlow", "WebSocket", "Docker"],
    image: "/thumbnails/healthpulse.png",
    featured: false,
  },
  {
    id: "invoicepro",
    title: "InvoicePro",
    description: "Automated invoicing for freelancers. Branded PDF invoices, payment tracking, reminder emails, Stripe/PayPal/bank transfer integration.",
    longDescription: "End-to-end invoicing SaaS with customizable templates, multi-currency, automated reminders, and 5+ payment gateway integrations.",
    category: ["web", "automation"],
    tags: ["SaaS", "Finance", "Automation"],
    tech: ["Next.js", "TypeScript", "Stripe", "PostgreSQL", "Resend", "Puppeteer", "Tailwind CSS"],
    image: "/thumbnails/invoicepro.png",
    featured: false,
  },
  {
    id: "langbridge",
    title: "LangBridge Translator",
    description: "Real-time translation for 40+ languages with context-aware neural translation. Voice input, camera OCR, and offline mode for 12 core languages.",
    longDescription: "Neural machine translation combining transformer models with domain-specific fine-tuning and multimodal input via speech and camera.",
    category: ["ai"],
    tags: ["AI", "NLP", "Translation"],
    tech: ["React Native", "PyTorch", "Hugging Face", "Whisper", "FastAPI", "ONNX Runtime"],
    image: "/thumbnails/langbridge.png",
    featured: false,
  },
  {
    id: "linkshort",
    title: "LinkShort Analytics",
    description: "URL shortener with enterprise analytics: click heatmaps, device fingerprinting, A/B redirect splits, custom branded domains. 1M+ redirects/day.",
    longDescription: "High-throughput URL shortening with edge-cached redirects, real-time analytics, geographic heatmaps, and branded domain support.",
    category: ["web"],
    tags: ["Analytics", "SaaS", "Performance"],
    tech: ["Go", "Redis", "PostgreSQL", "React", "Cloudflare Workers", "Chart.js"],
    image: "/thumbnails/linkshort.png",
    featured: false,
  },
  {
    id: "logismart",
    title: "LogiSmart Fleet",
    description: "Fleet management with real-time GPS, route optimization via OR-Tools, fuel analytics, and driver scoring. Manages 200+ vehicle fleets.",
    longDescription: "Fleet management platform with real-time tracking, route optimization, predictive maintenance, and driver analytics.",
    category: ["web"],
    tags: ["Logistics", "IoT", "Optimization"],
    tech: ["Next.js", "Python", "OR-Tools", "Mapbox", "PostgreSQL", "MQTT", "Redis"],
    image: "/thumbnails/logismart.png",
    featured: false,
  },
  {
    id: "melodai",
    title: "MelodAI Composer",
    description: "AI music generation from text prompts. 8 genres, multi-track layering, MIDI export, and a browser DAW for post-editing.",
    longDescription: "Text-to-music platform using fine-tuned MusicGen models with genre conditioning, multi-track arrangement, and MIDI/WAV export.",
    category: ["ai"],
    tags: ["AI", "Music", "Creative"],
    tech: ["Python", "MusicGen", "React", "Web Audio API", "FastAPI", "Tone.js"],
    image: "/thumbnails/melodai.png",
    featured: false,
  },
  {
    id: "mlpipeline",
    title: "MLPipeline Studio",
    description: "Visual ML pipeline builder — drag, connect, train, deploy. Data preprocessing, feature engineering, hyperparameter tuning, and one-click REST API deployment.",
    longDescription: "No-code ML pipeline orchestrator with visual DAG editor, automated feature engineering, distributed training, and containerized serving.",
    category: ["ai"],
    tags: ["ML", "Pipeline", "No-Code"],
    tech: ["React", "Python", "Ray", "MLflow", "FastAPI", "Docker", "PostgreSQL"],
    image: "/thumbnails/mlpipeline.png",
    featured: true,
  },
  {
    id: "newsagg",
    title: "NewsAgg Intelligence",
    description: "AI-curated news from 500+ sources. NLP deduplication, sentiment scoring, bias detection, and personalized feeds that learn from reading patterns.",
    longDescription: "News aggregation with transformer-based deduplication, summarization, political bias scoring, and collaborative filtering personalization.",
    category: ["ai", "web"],
    tags: ["AI", "NLP", "News"],
    tech: ["Next.js", "Python", "Hugging Face", "PostgreSQL", "Redis", "Celery", "Tailwind CSS"],
    image: "/thumbnails/newsagg.png",
    featured: false,
  },
  {
    id: "petcare",
    title: "PetCare Connect",
    description: "Pet platform connecting owners with vets, groomers, and sitters. AI symptom checker, vaccination reminders, and real-time GPS collar tracking.",
    longDescription: "Pet care marketplace with AI symptom triage, IoT collar GPS tracking, and automated health record management.",
    category: ["web"],
    tags: ["Marketplace", "Pet Tech", "IoT"],
    tech: ["React Native", "Node.js", "PostgreSQL", "OpenAI API", "Mapbox", "Firebase"],
    image: "/thumbnails/petcare.png",
    featured: false,
  },
  {
    id: "pixelwar",
    title: "PixelWar Arena",
    description: "Massively multiplayer browser game — thousands battle for territory on a shared pixel canvas. Real-time WebSocket updates, factions, 60fps Canvas rendering.",
    longDescription: "Large-scale multiplayer pixel territory game with WebSocket state sync, spatial partitioning, and Canvas rendering at 60fps.",
    category: ["game", "web"],
    tags: ["Game", "Multiplayer", "Canvas"],
    tech: ["TypeScript", "Canvas API", "WebSocket", "Go", "Redis", "PostgreSQL"],
    image: "/thumbnails/pixelwar.png",
    featured: false,
  },
  {
    id: "quizmaster",
    title: "QuizMaster AI",
    description: "Adaptive quiz platform generating questions from any document using LLMs. Spaced repetition, difficulty scaling, and classroom analytics for teachers.",
    longDescription: "AI adaptive learning with LLM question generation, SM-2 spaced repetition, and real-time classroom dashboards.",
    category: ["ai", "web"],
    tags: ["EdTech", "AI", "Adaptive Learning"],
    tech: ["Next.js", "OpenAI API", "PostgreSQL", "LangChain", "Chart.js", "Tailwind CSS"],
    image: "/thumbnails/quizmaster.png",
    featured: false,
  },
  {
    id: "racerx",
    title: "RacerX Turbo",
    description: "3D browser racing game with realistic physics, procedural tracks, multiplayer lobbies, and car customization. 60fps on mid-range hardware via WebGL.",
    longDescription: "WebGL racing game with Cannon.js physics, procedural track generation, WebRTC multiplayer, and optimized Three.js rendering.",
    category: ["game"],
    tags: ["Game", "3D", "WebGL"],
    tech: ["Three.js", "Cannon.js", "WebRTC", "TypeScript", "WebGL", "Node.js"],
    image: "/thumbnails/racerx.png",
    featured: false,
  },
  {
    id: "rentease",
    title: "RentEase Property",
    description: "Rental marketplace with 3D virtual tours, AI price recommendations, tenant screening, and automated lease generation. Smart contracts for deposits.",
    longDescription: "Real estate rental platform with 3D tours, ML pricing, digital lease signing, and optional blockchain escrow.",
    category: ["web"],
    tags: ["Real Estate", "Marketplace", "Web3"],
    tech: ["Next.js", "Python", "Three.js", "PostgreSQL", "Stripe", "Solidity", "Tailwind CSS"],
    image: "/thumbnails/rentease.png",
    featured: false,
  },
  {
    id: "resumeai",
    title: "ResumeAI Builder",
    description: "AI resume builder that analyzes job descriptions and tailors your resume for maximum ATS score. Targeted bullet points, skills matching, interview prep questions.",
    longDescription: "Resume optimization with JD parsing, ATS keyword matching, GPT-powered bullet generation, and multi-template PDF export.",
    category: ["ai", "web"],
    tags: ["AI", "Career", "SaaS"],
    tech: ["Next.js", "OpenAI API", "Puppeteer", "PostgreSQL", "TypeScript", "Tailwind CSS"],
    image: "/thumbnails/resumeai.png",
    featured: false,
  },
  {
    id: "secureauth",
    title: "SecureAuth Gateway",
    description: "Enterprise auth gateway with passwordless login, WebAuthn/FIDO2, adaptive MFA, device fingerprinting, and real-time brute-force detection. Drop-in Auth0 replacement.",
    longDescription: "Self-hosted IAM platform supporting OAuth2/OIDC, WebAuthn, TOTP, device trust scoring, and real-time threat detection.",
    category: ["web"],
    tags: ["Security", "Auth", "Enterprise"],
    tech: ["Go", "PostgreSQL", "Redis", "WebAuthn", "OAuth2", "Docker", "React"],
    image: "/thumbnails/secureauth.png",
    featured: true,
  },
  {
    id: "shopengine",
    title: "ShopEngine Commerce",
    description: "Headless e-commerce with AI recommendations, dynamic pricing, 4-channel inventory sync, and sub-200ms API response times.",
    longDescription: "High-performance headless commerce with GraphQL API, ML recommendation engine, and multi-channel inventory management.",
    category: ["web", "ai"],
    tags: ["E-Commerce", "AI", "Headless"],
    tech: ["Node.js", "GraphQL", "PostgreSQL", "Redis", "React", "Stripe", "Docker"],
    image: "/thumbnails/shopengine.png",
    featured: false,
  },
  {
    id: "smartpark",
    title: "SmartPark IoT",
    description: "Smart parking with ultrasonic sensors and plate recognition. Real-time slot availability on mobile, automated billing, and operator analytics.",
    longDescription: "IoT smart parking with ultrasonic occupancy sensors, ALPR integration, and automated billing via NFC/QR.",
    category: ["web"],
    tags: ["IoT", "Smart City", "Mobile"],
    tech: ["React Native", "Python", "MQTT", "OpenCV", "PostgreSQL", "Raspberry Pi", "Node.js"],
    image: "/thumbnails/smartpark.png",
    featured: false,
  },
  {
    id: "socialbot",
    title: "SocialBot Manager",
    description: "Cross-platform social media automation: scheduled posts, AI captions, hashtag optimization, engagement analytics, automated DM responses. 20+ accounts.",
    longDescription: "Social media management with multi-account scheduling, GPT captions, engagement prediction, and unified analytics.",
    category: ["automation", "ai"],
    tags: ["Social Media", "AI", "Automation"],
    tech: ["Next.js", "Python", "OpenAI API", "Redis", "PostgreSQL", "Bull Queue", "Tailwind CSS"],
    image: "/thumbnails/socialbot.png",
    featured: false,
  },
  {
    id: "stocksense",
    title: "StockSense Predictor",
    description: "ML stock analysis with LSTM price prediction, news sentiment analysis, technical indicators, and backtested portfolio strategies with Sharpe ratio tracking.",
    longDescription: "Quantitative stock analysis combining LSTM prediction, NLP sentiment, 30+ technical indicators, and Monte Carlo simulation.",
    category: ["ai"],
    tags: ["Finance", "ML", "Analytics"],
    tech: ["Python", "TensorFlow", "Pandas", "React", "FastAPI", "PostgreSQL", "D3.js"],
    image: "/thumbnails/stocksense.png",
    featured: false,
  },
  {
    id: "taskflow",
    title: "TaskFlow Kanban",
    description: "Project management with AI task estimation, dependency graphs, automated sprint planning, and Slack/GitHub integration. Linear meets AI.",
    longDescription: "Intelligent PM with drag-and-drop Kanban, AI story point estimation, critical path analysis, and deep developer tool integrations.",
    category: ["web", "ai"],
    tags: ["Productivity", "AI", "SaaS"],
    tech: ["Next.js", "TypeScript", "PostgreSQL", "OpenAI API", "Socket.io", "Tailwind CSS"],
    image: "/thumbnails/taskflow.png",
    featured: false,
  },
  {
    id: "videochat",
    title: "VideoChat HD",
    description: "P2P video conferencing with AI noise cancellation, real-time captions, screen sharing, virtual backgrounds, and breakout rooms. 50 participants, zero dependencies.",
    longDescription: "WebRTC video conferencing with SFU architecture, RNNoise suppression, Whisper live captions, and virtual background segmentation.",
    category: ["web"],
    tags: ["Video", "WebRTC", "Real-Time"],
    tech: ["React", "WebRTC", "Node.js", "mediasoup", "Whisper", "TensorFlow.js", "Tailwind CSS"],
    image: "/thumbnails/videochat.png",
    featured: false,
  },
  {
    id: "voiceclone",
    title: "VoiceClone Studio",
    description: "Clone any voice from 30 seconds of audio. TTS with emotion control, multilingual support, and real-time voice conversion. For dubbing, podcasts, and accessibility.",
    longDescription: "Voice cloning using VITS-based TTS with speaker embedding, emotion conditioning, and cross-lingual transfer.",
    category: ["ai"],
    tags: ["AI", "Voice", "TTS"],
    tech: ["Python", "PyTorch", "VITS", "FastAPI", "React", "Web Audio API", "Docker"],
    image: "/thumbnails/voiceclone.png",
    featured: false,
  },
  {
    id: "weathernow",
    title: "WeatherNow Hyperlocal",
    description: "Hyperlocal weather with 500m grid resolution, 15-minute nowcasting, severe alerts, and agricultural insights. Radar + satellite + ML models.",
    longDescription: "Hyperlocal forecasting fusing radar, satellite, and ground station data through ensemble ML for 500m-resolution nowcasting.",
    category: ["web"],
    tags: ["Weather", "ML", "Mobile"],
    tech: ["React Native", "Python", "TensorFlow", "PostGIS", "Mapbox", "FastAPI", "Redis"],
    image: "/thumbnails/weathernow.png",
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
  "Tech Enthusiast",
  "Full-Stack Developer",
  "AI Engineer",
  "Game Developer",
  "UI/UX Designer",
  "Automation Builder",
  "Problem Solver",
];
