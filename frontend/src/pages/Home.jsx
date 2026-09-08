import { Link } from 'react-router-dom'

const HELPS = [
    { n: '01', title: 'Tell us about yourself', desc: 'Interests, skills, academics, and work preferences.' },
    { n: '02', title: 'See your strongest career areas', desc: 'Get career areas that match your profile and understand why.' },
    { n: '03', title: 'Explore a specific direction', desc: 'Move from domain → role → specialization.' },
    { n: '04', title: 'Know what to work on next', desc: 'See your skill gaps and practical next steps.' },
]

const Home = () => (
    <div className="px-4">
        {/* ============================================================ */}
        {/* HERO */}
        {/* ============================================================ */}
        <section className="max-w-3xl mx-auto pt-14 pb-16 md:pt-20 md:pb-20 text-center">
            <div className="animate-fade-in">
                <span className="text-xs font-semibold uppercase tracking-widest text-secondary">
                    Career exploration, made clear
                </span>
                <h1 className="text-4xl md:text-[2.75rem] leading-tight font-extrabold text-ink mt-3 mb-5">
                    Find a career path that fits you.
                </h1>
                <p className="text-ink-soft text-base md:text-lg leading-relaxed mb-8 max-w-lg mx-auto">
                    Tell us what you enjoy, what you're good at, and how you like to work.
                    We'll help you explore career paths, specializations, and what to
                    work on next.
                </p>
                <div className="flex flex-wrap items-center justify-center gap-3 mb-3">
                    <Link to="/recommend" className="btn-primary no-underline inline-block">
                        Find Careers for Me
                    </Link>
                    <Link to="/explore" className="btn-outline no-underline inline-block">
                        Explore Careers
                    </Link>
                </div>
                <p className="text-ink-muted text-xs">
                    About 4 minutes · No career knowledge needed
                </p>
            </div>
        </section>

        {/* ============================================================ */}
        {/* HOW CAREER NAVIGATOR HELPS (why + how, merged) */}
        {/* ============================================================ */}
        <section className="max-w-6xl mx-auto py-12 md:py-14 border-t border-line">
            <h2 className="text-2xl font-bold text-ink text-center mb-8">
                How Career Navigator helps
            </h2>
            <div className="grid grid-cols-1 md:grid-cols-4 gap-5">
                {HELPS.map(s => (
                    <div key={s.n}>
                        <div className="w-8 h-8 rounded-lg bg-primary/10 text-primary font-bold text-sm
                                        flex items-center justify-center mb-3">
                            {s.n}
                        </div>
                        <h3 className="text-ink font-bold mb-1.5 text-sm">{s.title}</h3>
                        <p className="text-ink-muted text-sm leading-relaxed">{s.desc}</p>
                    </div>
                ))}
            </div>
        </section>

        {/* ============================================================ */}
        {/* FINAL CTA */}
        {/* ============================================================ */}
        <section className="max-w-6xl mx-auto py-12 md:py-14">
            <div className="rounded-2xl bg-primary px-6 py-10 md:py-12 text-center">
                <h2 className="text-2xl font-bold text-white mb-2.5">
                    You don't need to know the answer yet.
                </h2>
                <p className="text-white/70 text-base mb-6 max-w-md mx-auto">
                    Start with what you know about yourself. We'll help you explore from there.
                </p>
                <div className="flex flex-wrap items-center justify-center gap-3">
                    <Link to="/recommend"
                          className="no-underline inline-block font-semibold rounded-xl px-5 py-2.5
                                     bg-accent text-ink hover:brightness-95 transition-all">
                        Find Careers for Me
                    </Link>
                    <Link to="/explore"
                          className="no-underline inline-block font-semibold rounded-xl px-5 py-2.5
                                     border border-white/30 text-white hover:bg-white/10 transition-colors">
                        Explore Careers
                    </Link>
                </div>
            </div>
        </section>

        {/* ============================================================ */}
        {/* FOOTER */}
        {/* ============================================================ */}
        <footer className="max-w-6xl mx-auto py-8 border-t border-line text-center">
            <div className="flex items-center justify-center gap-2 mb-1.5">
                <span className="text-lg">🧭</span>
                <span className="text-ink font-bold text-sm">Career Navigator</span>
            </div>
            <p className="text-ink-muted text-xs">
                Career exploration and recommendation for students. · Final Year Project
            </p>
        </footer>
    </div>
)

export default Home
