"use client";
import { useEffect, useRef, useState } from "react";

/** Toont korte meldingen, bijv. als een koppeling nog niet is ingesteld. */
export function showNotice(message: string) {
  window.dispatchEvent(new CustomEvent("roots-notice", { detail: message }));
}

export default function Notice() {
  const [msg, setMsg] = useState("");
  const [visible, setVisible] = useState(false);
  const timer = useRef<ReturnType<typeof setTimeout>>(undefined);
  useEffect(() => {
    const on = (e: Event) => {
      setMsg((e as CustomEvent<string>).detail);
      setVisible(true);
      clearTimeout(timer.current);
      timer.current = setTimeout(() => setVisible(false), 5200);
    };
    window.addEventListener("roots-notice", on);
    return () => window.removeEventListener("roots-notice", on);
  }, []);
  return (
    <div className={"notice" + (visible ? " is-visible" : "")} role="status" aria-live="polite">
      {msg}
    </div>
  );
}
