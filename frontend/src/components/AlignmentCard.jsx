const COLORS = ['#2f7dfa', '#38bdf8', '#60a5fa']
const RANK_LABEL = ['Best match', '2nd match', '3rd match']
const CONFIDENCE_STYLE = {
    Strong: 'bg-green-500/15 text-green-400',
    Possible: 'bg-amber-500/15 text-amber-400',
    Weak: 'bg-line text-ink-muted',
    // legacy labels, kept so older cached responses don't break mid-transition
    High: 'bg-green-500/15 text-green-400',
    Medium: 'bg-amber-500/15 text-amber-400',
    Low: 'bg-line text-ink-muted',
}
const MATCH_LABEL = {
    Strong: 'Strong Match', Possible: 'Possible Match', Weak: 'Closest Match',
    High: 'Strong Match', Medium: 'Possible Match', Low: 'Closest Match',
}
const BREAKDOWN_ROWS = [
    ['interest_fit', 'Interest Fit'], ['preference_fit', 'Work Style Fit'],
    ['skill_fit', 'Skill Fit'], ['academic_fit', 'Academic Fit'], ['model_signal', 'Model Signal'],
]

const AlignmentCard = ({ item, index, label, isActive, onClick, ctaLabel, breakdown, exploreRoles }) => (
    <button
        onClick={onClick}
        className={`card text-left transition-all duration-200 w-full
            ${isActive ? 'border-primary ring-2 ring-primary/20' : 'hover:border-line-strong'}`}
    >
        <div className="flex items-center justify-between mb-2 gap-2">
            <span className="text-[11px] font-semibold uppercase tracking-wide text-ink-muted">
                {RANK_LABEL[index] || `Match ${index + 1}`}
            </span>
            {item.confidence && (
                <span className={`text-[10px] font-semibold uppercase tracking-wide px-2 py-0.5 rounded-full
                                   ${CONFIDENCE_STYLE[item.confidence] || CONFIDENCE_STYLE.Weak}`}>
                    {MATCH_LABEL[item.confidence] || item.confidence}
                </span>
            )}
        </div>
        <h3 className="text-ink font-bold mb-1 text-sm">{label}</h3>
        <div className="text-2xl font-black mb-2" style={{ color: COLORS[index % 3] }}>
            {item.alignment_pct}% <span className="text-sm font-semibold">profile alignment</span>
        </div>
        <div className="h-1.5 bg-line rounded-full mb-3">
            <div className="h-full rounded-full"
                 style={{ width: `${item.alignment_pct}%`, background: COLORS[index % 3] }} />
        </div>
        {item.explanation && item.explanation.length > 0 && (
            <>
                <div className="text-[11px] font-semibold text-ink-soft mb-1">Why this matches</div>
                <ul className="text-xs text-ink-muted space-y-1">
                    {item.explanation.map((reason, i) => (
                        <li key={i} className="leading-snug flex gap-1.5">
                            <span className="text-green-400 shrink-0">✓</span>
                            <span>{reason}</span>
                        </li>
                    ))}
                </ul>
            </>
        )}
        {breakdown && (
            <div className="mt-3 pt-3 border-t border-line space-y-1.5">
                {BREAKDOWN_ROWS.map(([key, rowLabel]) => (
                    <div key={key} className="flex items-center gap-2">
                        <span className="text-[10px] text-ink-muted w-24 shrink-0">{rowLabel}</span>
                        <div className="flex-1 h-1 bg-line rounded-full">
                            <div className="h-full rounded-full bg-secondary/60"
                                 style={{ width: `${Math.min(100, breakdown[key])}%` }} />
                        </div>
                        <span className="text-[10px] text-ink-soft font-semibold w-8 text-right">
                            {Math.round(breakdown[key])}%
                        </span>
                    </div>
                ))}
            </div>
        )}
        {exploreRoles && exploreRoles.length > 0 && (
            <div className="mt-3 pt-3 border-t border-line">
                <div className="text-[11px] font-semibold text-ink-soft mb-1.5">What you can explore</div>
                <div className="flex flex-wrap gap-1">
                    {exploreRoles.map(r => (
                        <span key={r} className="text-[10px] px-2 py-0.5 rounded-full bg-paper border border-line text-ink-muted">
                            {r}
                        </span>
                    ))}
                </div>
            </div>
        )}
        {ctaLabel && !isActive && (
            <div className="text-xs font-semibold text-primary mt-3">{ctaLabel}</div>
        )}
    </button>
)

export default AlignmentCard
