import type { Content } from "@/content/nl";
import { siteConfig } from "@/config/site";

export function Eyebrow({ step, label }: { step?: string; label: string }) {
  return <p className="eyebrow">{step && <span className="step">{step}</span>} {label}</p>;
}

export function PriceLine({ c }: { c: Content }) {
  const line = siteConfig[c.lang].challengePrijsRegel;
  return line ? <p className="price-line">{line}</p> : null;
}

export function CoverPlaceholder({ c, small }: { c: Content; small?: boolean }) {
  const p = c.handbook.coverPlaceholder;
  return (
    <div className="cover-placeholder" role={small ? undefined : "img"} aria-label={small ? undefined : c.handbook.coverAlt}>
      <span className="t1">{p.t1}</span>
      <span className="t2">{p.t2}</span>
      <span className="t3">{p.t3}</span>
      {!small && <span className="ph-label">{p.label}</span>}
    </div>
  );
}

export function MasterclassVideo({ c }: { c: Content }) {
  const url = siteConfig[c.lang].masterclassVideoUrl;
  return (
    <div className={"video" + (url ? " has-video" : "")}>
      {url ? (
        <iframe src={url} title={c.ui.videoTitle} allow="autoplay; fullscreen; picture-in-picture" allowFullScreen loading="lazy" />
      ) : (
        <div className="ph">
          <div className="play" aria-hidden="true" />
          {c.ui.videoPlaceholder}<br /><code>{c.ui.videoPlaceholderHint}</code>
        </div>
      )}
    </div>
  );
}
