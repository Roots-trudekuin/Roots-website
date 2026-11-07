import type { ReactNode } from "react";
import RootLayout from "@/components/RootLayout";
import "../globals.css";

export default function Layout({ children }: { children: ReactNode }) {
  return <RootLayout lang="nl">{children}</RootLayout>;
}
