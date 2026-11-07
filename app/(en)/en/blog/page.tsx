import type { Metadata } from "next";
import { en as c } from "@/content/en";
import BlogPage from "@/components/BlogPage";

export const metadata: Metadata = { title: c.blog.metaTitle };

export default function Page() {
  return <BlogPage c={c} />;
}
