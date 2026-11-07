import type { Metadata } from "next";
import { nl as c } from "@/content/nl";
import MasterclassPage from "@/components/MasterclassPage";

export const metadata: Metadata = {
  title: c.meta.masterclassTitle,
  description: c.meta.masterclassDescription,
};

export default function Page() {
  return <MasterclassPage c={c} />;
}
