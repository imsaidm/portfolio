"use client";

import dynamic from "next/dynamic";

const ScrollCompanion = dynamic(() => import("@/components/ScrollCompanion"), { ssr: false });

export default function ScrollCompanionWrapper() {
    return <ScrollCompanion />;
}
