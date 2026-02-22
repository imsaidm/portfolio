import Navbar from "@/components/Navbar";
import Hero from "@/components/Hero";
import About from "@/components/About";
import Skills from "@/components/Skills";
import TechMarquee from "@/components/TechMarquee";
import Projects from "@/components/Projects";
import Contact from "@/components/Contact";
import Footer from "@/components/Footer";
import CursorGlow from "@/components/CursorGlow";
import LoadingScreen from "@/components/LoadingScreen";
import ScrollCompanionWrapper from "@/components/ScrollCompanionWrapper";
import ScrollToTop from "@/components/ScrollToTop";

export default function Home() {
  return (
    <>
      <LoadingScreen />
      <CursorGlow />
      <ScrollToTop />
      <ScrollCompanionWrapper />
      <div className="noise-overlay" />
      <Navbar />
      <main className="relative z-10">
        <Hero />
        <About />
        <div className="section-divider" />
        <Skills />
        <TechMarquee />
        <div className="section-divider" />
        <Projects />
        <div className="section-divider" />
        <Contact />
      </main>
      <Footer />
    </>
  );
}
