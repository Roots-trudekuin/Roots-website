import type { Metadata } from "next";
import { en as c } from "@/content/en";
import MasterclassPage from "@/components/MasterclassPage";

export const metadata: Metadata = {
  title: c.meta.masterclassTitle,
  description: c.meta.masterclassDescription,
};

export default function Page() {
  return <MasterclassPage c={c} />;
}
