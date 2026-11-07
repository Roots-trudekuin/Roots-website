import type { Metadata } from "next";
import { nl as c } from "@/content/nl";
import HomePage from "@/components/HomePage";

export const metadata: Metadata = {
  title: c.meta.homeTitle,
  description: c.meta.homeDescription,
};

export default function Page() {
  return <HomePage c={c} />;
}
