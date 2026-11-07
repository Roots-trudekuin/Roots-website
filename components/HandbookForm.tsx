"use client";
import { useRef, useState, type FormEvent } from "react";
import type { Content } from "@/content/nl";
import { siteConfig } from "@/config/site";

/** Handboekformulier. Verstuurt alleen echt als emailMarketing.formAction is ingesteld. */
export default function HandbookForm({ c }: { c: Content }) {
  const [status, setStatus] = useState<{ msg: string; type: "" | "error" | "pending" }>({ msg: "", type: "" });
  const [invalid, setInvalid] = useState({ name: false, email: false });
  const [busy, setBusy] = useState(false);
  const nameRef = useRef<HTMLInputElement>(null);
  const emailRef = useRef<HTMLInputElement>(null);

  function onSubmit(e: FormEvent) {
    e.preventDefault();
    const name = nameRef.current!, email = emailRef.current!;
    const inv = {
      name: name.value.trim() === "",
      email: email.value.trim() === "" || !email.checkValidity(),
    };
    setInvalid(inv);
    if (inv.name || inv.email) {
      setStatus({ msg: c.ui.invalid, type: "error" });
      (inv.name ? name : email).focus();
      return;
    }
    const M = siteConfig[c.lang].emailMarketing;
    if (!M.formAction) {
      setStatus({ msg: c.ui.noForm, type: "pending" });
      return;
    }
    // Gewone formulierpost naar de e-maildienst; die mailt het handboek en stuurt door naar de bedankpagina.
    const out = document.createElement("form");
    out.method = M.method;
    out.action = M.formAction;
    out.style.display = "none";
    const add = (n: string, v: string) => {
      const i = document.createElement("input");
      i.type = "hidden"; i.name = n; i.value = v; out.appendChild(i);
    };
    add(M.nameField, name.value.trim());
    add(M.emailField, email.value.trim());
    Object.entries(M.hiddenFields).forEach(([k, v]) => add(k, v));
    document.body.appendChild(out);
    setStatus({ msg: c.ui.sending, type: "pending" });
    setBusy(true);
    out.submit();
  }

  return (
    <form className="form" id={c.ids.form} noValidate onSubmit={onSubmit}>
      <div className="form-row">
        <label htmlFor="hb-naam">{c.handbook.nameLabel}</label>
        <input id="hb-naam" ref={nameRef} name="naam" type="text" autoComplete="given-name" required aria-invalid={invalid.name} />
      </div>
      <div className="form-row">
        <label htmlFor="hb-email">{c.handbook.emailLabel}</label>
        <input id="hb-email" ref={emailRef} name="email" type="email" autoComplete="email" inputMode="email" required aria-invalid={invalid.email} />
      </div>
      <button className="btn btn-primary" type="submit" disabled={busy}>{c.handbook.submit}</button>
      <p className={"form-status" + (status.type ? " is-" + status.type : "")} role="status" aria-live="polite">{status.msg}</p>
    </form>
  );
}
