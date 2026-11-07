import type { Metadata } from "next";
import { nl as c } from "@/content/nl";
import BlogPage from "@/components/BlogPage";

export const metadata: Metadata = { title: c.blog.metaTitle };

export default function Page() {
  return <BlogPage c={c} />;
}
