import type { Metadata } from "next";
import { Inter, Space_Grotesk, JetBrains_Mono } from "next/font/google";
import "./globals.css";

const inter = Inter({
  variable: "--font-inter",
  subsets: ["latin"],
  display: "swap",
});

const spaceGrotesk = Space_Grotesk({
  variable: "--font-space-grotesk",
  subsets: ["latin"],
  display: "swap",
});

const jetbrainsMono = JetBrains_Mono({
  variable: "--font-jetbrains-mono",
  subsets: ["latin"],
  display: "swap",
});

export const metadata: Metadata = {
  title: "Said Mustaqim - Tech Enthusiast & Full-Stack Developer",
  description:
    "Portfolio of Said Mustaqim — A tech enthusiast mastering fullstack development, UI/UX design, AI engineering, and game development. Crafting digital experiences that push boundaries.",
  keywords: [
    "Said Mustaqim",
    "portfolio",
    "fullstack developer",
    "full-stack developer",
    "UI/UX designer",
    "AI engineer",
    "game developer",
    "tech enthusiast",
  ],
  authors: [{ name: "Said Mustaqim" }],
  creator: "Said Mustaqim",
  robots: { index: true, follow: true },
  openGraph: {
    title: "Said Mustaqim - Tech Enthusiast & Full-Stack Developer",
    description:
      "A tech enthusiast mastering fullstack, UI/UX, AI, and game development. Building things that live on the internet.",
    type: "website",
    locale: "en_US",
    siteName: "Said Mustaqim Portfolio",
  },
  twitter: {
    card: "summary_large_image",
    title: "Said Mustaqim - Tech Enthusiast & Full-Stack Developer",
    description:
      "A tech enthusiast mastering fullstack, UI/UX, AI, and game development.",
    creator: "@imsaidm",
  },
  other: {
    "theme-color": "#0a0a0a",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="scroll-smooth" suppressHydrationWarning>
      <body
        className={`${inter.variable} ${spaceGrotesk.variable} ${jetbrainsMono.variable} antialiased`}
        style={{ fontFamily: "var(--font-inter), system-ui, sans-serif" }}
      >
        {children}
      </body>
    </html>
  );
}
