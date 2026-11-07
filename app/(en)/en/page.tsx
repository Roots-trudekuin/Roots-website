import type { Metadata } from "next";
import { en as c } from "@/content/en";
import HomePage from "@/components/HomePage";

export const metadata: Metadata = {
  title: c.meta.homeTitle,
  description: c.meta.homeDescription,
};

export default function Page() {
  return <HomePage c={c} />;
}
