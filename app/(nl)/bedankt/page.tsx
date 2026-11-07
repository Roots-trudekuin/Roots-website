import type { Metadata } from "next";
import { nl as c } from "@/content/nl";
import ThanksPage from "@/components/ThanksPage";

export const metadata: Metadata = {
  title: c.meta.thanksTitle,
  robots: { index: false },
};

export default function Page() {
  return <ThanksPage c={c} />;
}
