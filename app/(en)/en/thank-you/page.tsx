import type { Metadata } from "next";
import { en as c } from "@/content/en";
import ThanksPage from "@/components/ThanksPage";

export const metadata: Metadata = {
  title: c.meta.thanksTitle,
  robots: { index: false },
};

export default function Page() {
  return <ThanksPage c={c} />;
}
