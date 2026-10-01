import { useState, useEffect, useRef } from 'react'
import api from '../api/axiosConfig'
import AlignmentCard from '../components/AlignmentCard'

const STRENGTH_GROUPS = [
    { title: 'Thinking', skills: [
        ['problem_solving', 'Problem Solving'], ['analytical_thinking', 'Analytical Thinking'], ['research', 'Research'],
    ] },
    { title: 'Working With Others', skills: [
        ['communication', 'Communication'], ['leadership', 'Leadership'],
        ['teamwork', 'Teamwork'], ['presentation', 'Presentation'],
    ] },
    { title: 'Making & Organizing', skills: [
        ['creativity', 'Creativity'], ['technical_ability', 'Technical Ability'], ['organization', 'Organization'],
    ] },
]
const SCORES = [
    ['math_score', 'Mathematics'], ['science_score', 'Science'], ['english_score', 'English'],
    ['computer_score', 'Computer'], ['business_score', 'Business/Economics'], ['arts_score', 'Arts'],
]
const PREFS = [
    ['pref_people_vs_independent', 'Independent work', 'Working with people'],
    ['pref_creative_vs_analytical', 'Analytical', 'Creative'],
    ['pref_indoor_vs_outdoor', 'Indoor', 'Outdoor'],
    ['pref_structured_vs_flexible', 'Structured', 'Flexible'],
    ['pref_handson_vs_theoretical', 'Theoretical', 'Hands-on'],
    ['pref_tech_vs_people', 'Tech-oriented', 'People-oriented'],
]
const SKILL_ANCHORS = ['Beginner', 'Developing', 'Comfortable', 'Strong', 'Very Strong']
const EDUCATION_LEVELS = ['+2 / High School', 'Bachelor', 'Master']
const STEPS = ['About You', 'Strengths', 'Work Style', 'Interests', 'Review']
const NEUTRAL_SCORE = 65
const TOOL_LEVELS = [{ v: 0, label: 'Not used' }, { v: 2, label: 'Tried' }, { v: 4, label: 'Comfortable' }]
const COUNT_OPTIONS = [
    { n: 1, label: '1 career', desc: 'Just my strongest match' },
    { n: 2, label: '2 careers', desc: 'A couple of options to compare' },
    { n: 3, label: '3 careers', desc: 'A broader look' },
]

// The number the user picks is a MAXIMUM, not a target -- the backend
// only ever returns domains that actually clear its alignment threshold,
// so this message has to explain whatever combination of
// requested/qualified/returned actually happened, honestly.
const buildResultMessage = (meta, results) => {
    if (!meta) return null
    if (meta.fallback) {
        const best = results[0]
        return `None of the career areas reached a strong enough alignment with your current profile. `
            + `Your closest match is ${best.domain} at ${best.alignment_pct}%. You may want to adjust `
            + `your interests or explore careers before trying again.`
    }
    let base
    if (meta.returned_count === 1) base = 'Your profile shows one clear career match.'
    else if (meta.returned_count === 2) base = 'Your profile shows 2 meaningful career matches.'
    else base = `Here are your ${meta.returned_count} strongest career areas.`

    if (meta.returned_count < meta.requested_count) {
        base += ` You asked for up to ${meta.requested_count} recommendations, but only `
            + `${meta.returned_count} passed the current alignment threshold.`
    }
    return base
}

const INITIAL_FORM = {
    name: '', education_level: 'Bachelor',
    communication: 3, problem_solving: 3, creativity: 3, analytical_thinking: 3,
    leadership: 3, teamwork: 3, technical_ability: 3, research: 3,
    organization: 3, presentation: 3,
    math_score: 70, science_score: 70, english_score: 70,
    computer_score: 70, business_score: 70, arts_score: 70,
    pref_people_vs_independent: 3, pref_creative_vs_analytical: 3,
    pref_indoor_vs_outdoor: 3, pref_structured_vs_flexible: 3,
    pref_handson_vs_theoretical: 3, pref_tech_vs_people: 3,
}

const Slider = ({ label, value, onChange, min = 1, max = 5, leftLabel, rightLabel, anchors, disabled }) => (
    <div className={`mb-4 ${disabled ? 'opacity-40' : ''}`}>
        <div className="flex justify-between text-sm mb-1">
            <span className="text-ink-soft">{label}</span>
            <span className="text-primary font-bold">
                {disabled ? 'N/A' : `${value}${anchors ? ` · ${anchors[value - 1]}` : ''}`}
            </span>
        </div>
        <input type="range" min={min} max={max} value={value} disabled={disabled}
               onChange={e => onChange(Number(e.target.value))}
               className="w-full accent-primary" />
        {leftLabel && (
            <div className="flex justify-between text-xs text-ink-muted mt-1">
                <span>{leftLabel}</span><span>{rightLabel}</span>
            </div>
        )}
    </div>
)

const Recommend = () => {
    const [step, setStep] = useState(0)
    const [form, setForm] = useState(INITIAL_FORM)
    const [naSubjects, setNaSubjects] = useState(new Set())
    const [interestTaxonomy, setInterestTaxonomy] = useState(null)
    const [interests, setInterests] = useState({})
    const [curiousTags, setCuriousTags] = useState(new Set())
    const [customInterest, setCustomInterest] = useState('')
    const [customInterests, setCustomInterests] = useState([])
    const [openTagDomain, setOpenTagDomain] = useState(null)
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)
    const [recommendationCount, setRecommendationCount] = useState(3)

    // Results phase state
    const [domainResults, setDomainResults] = useState(null)
    const [domainMeta, setDomainMeta] = useState(null)
    const [selectedDomain, setSelectedDomain] = useState(null)
    const [roleResults, setRoleResults] = useState(null)
    const [selectedRole, setSelectedRole] = useState(null)
    const [specResults, setSpecResults] = useState(null)
    const [selectedSpec, setSelectedSpec] = useState(null)
    const [roleDetail, setRoleDetail] = useState(null)
    const [toolAnswers, setToolAnswers] = useState({})
    const [gapResult, setGapResult] = useState(null)
    const [roadmapResult, setRoadmapResult] = useState(null)

    const domainSectionRef = useRef(null)
    const roleSectionRef = useRef(null)

    useEffect(() => {
        api.get('/api/explorer/interests').then(res => setInterestTaxonomy(res.data.interest_taxonomy))
    }, [])

    const update = (name, value) => setForm(prev => ({ ...prev, [name]: value }))

    const toggleNA = (key) => {
        setNaSubjects(prev => {
            const next = new Set(prev)
            if (next.has(key)) next.delete(key)
            else { next.add(key); update(key, NEUTRAL_SCORE) }
            return next
        })
    }

    // First click = "interested" (2), not the weakest possible value --
    // a single tap is the natural action, so it should register as a
    // real, meaningful signal. Second click bumps to "very interested"
    // (3); third click clears it. Setting real interest clears any
    // "curious" flag on the same tag (they're mutually exclusive).
    const cycleTag = (tag) => {
        setInterests(prev => {
            const current = prev[tag] || 0
            const next = current === 0 ? 2 : current === 2 ? 3 : 0
            const copy = { ...prev }
            if (next === 0) delete copy[tag]
            else copy[tag] = next
            return copy
        })
        setCuriousTags(prev => {
            if (!prev.has(tag)) return prev
            const next = new Set(prev); next.delete(tag); return next
        })
    }

    // "Curious to explore" -- for a tag you haven't committed real
    // interest to yet. Counts for only a small, capped amount of
    // interest score server-side (see hybrid_scoring.py) -- nowhere
    // near "very interested" -- and doesn't count toward the 3-interest
    // minimum below.
    const toggleCurious = (tag, e) => {
        e.stopPropagation()
        setCuriousTags(prev => {
            const next = new Set(prev)
            if (next.has(tag)) next.delete(tag)
            else next.add(tag)
            return next
        })
    }

    const addCustomInterest = () => {
        const val = customInterest.trim()
        if (val && !customInterests.includes(val)) {
            setCustomInterests(prev => [...prev, val])
        }
        setCustomInterest('')
    }

    const handleNext = () => {
        if (step === 3 && Object.keys(interests).length < 3) {
            setError('Choose at least 3 interests to help us understand you better')
            return
        }
        setError(null)
        setStep(s => s + 1)
    }

    const buildStudentPayload = (tools) => ({
        ...form, interests, tools: tools ?? {},
        curious_interests: [...curiousTags], na_subjects: [...naSubjects],
    })

    const handleSubmit = async () => {
        setLoading(true)
        setError(null)
        try {
            const res = await api.post('/api/recommend/domain', {
                student: buildStudentPayload(), recommendation_count: recommendationCount,
            })
            setDomainResults(res.data.recommendations)
            setDomainMeta({
                requested_count: res.data.requested_count,
                qualified_count: res.data.qualified_count,
                returned_count: res.data.returned_count,
                fallback: res.data.fallback,
            })
       } catch (err) {
    console.error('DOMAIN ERROR:', err)
    console.error('BACKEND RESPONSE:', err.response?.data)

    setError(
        err.response?.data?.detail ||
        'Could not get recommendations.'
    )
} finally {
            setLoading(false)
        }
    }

    const pickDomain = async (domain) => {
        setSelectedDomain(domain)
        setSelectedRole(null); setRoleResults(null); setRoleDetail(null)
        setSelectedSpec(null); setSpecResults(null)
        setToolAnswers({}); setGapResult(null); setRoadmapResult(null)
        setLoading(true)
        try {
            const res = await api.post('/api/recommend/role', { student: buildStudentPayload(), domain })
            setRoleResults(res.data.recommendations)
        } catch (err) {
            setError('Could not get role recommendations.')
        } finally {
            setLoading(false)
        }
    }

    const loadRoleDetail = async (domain, role, specialization) => {
        try {
            const res = await api.get('/api/recommend/role-detail', { params: { domain, role, specialization } })
            setRoleDetail(res.data)
        } catch (err) {
            setRoleDetail(null)
        }
    }

    const pickRole = async (role) => {
        setSelectedRole(role)
        setSelectedSpec(null); setToolAnswers({})
        setGapResult(null); setRoadmapResult(null)
        setLoading(true)
        try {
            const [specRes] = await Promise.all([
                api.post('/api/recommend/specialization', { student: buildStudentPayload(), domain: selectedDomain, role }),
                loadRoleDetail(selectedDomain, role, null),
            ])
            if (specRes.data.specializations.length > 0) {
                setSpecResults(specRes.data.specializations)
            } else {
                setSpecResults(null)
                await loadGapAndRoadmap(selectedDomain, role, null, {})
            }
        } catch (err) {
            setError('Could not get specialization data.')
        } finally {
            setLoading(false)
        }
    }

    const pickSpecialization = async (spec) => {
        setSelectedSpec(spec)
        setToolAnswers({})
        await Promise.all([
            loadGapAndRoadmap(selectedDomain, selectedRole, spec, {}),
            loadRoleDetail(selectedDomain, selectedRole, spec),
        ])
    }

    const loadGapAndRoadmap = async (domain, role, specialization, tools) => {
        setLoading(true)
        try {
            const payload = { student: buildStudentPayload(tools), domain, role, specialization }
            const [gapRes, roadmapRes] = await Promise.all([
                api.post('/api/recommend/skill-gap', payload),
                api.post('/api/recommend/roadmap', payload),
            ])
            setGapResult(gapRes.data)
            setRoadmapResult(roadmapRes.data)
        } catch (err) {
            setError('Could not load skill gap / roadmap.')
        } finally {
            setLoading(false)
        }
    }

    // A tool level changed -- recompute skill-gap/roadmap immediately so
    // self-assessed experience actually changes the result.
    const setToolLevel = (tool, value) => {
        const next = { ...toolAnswers }
        if (value === 0) delete next[tool]
        else next[tool] = value
        setToolAnswers(next)
        loadGapAndRoadmap(selectedDomain, selectedRole, selectedSpec, next)
    }

    const resetAll = () => {
        setStep(0); setForm(INITIAL_FORM); setNaSubjects(new Set())
        setInterests({}); setCuriousTags(new Set()); setCustomInterests([])
        setRecommendationCount(3)
        setDomainResults(null); setDomainMeta(null); setSelectedDomain(null); setRoleResults(null)
        setSelectedRole(null); setSpecResults(null); setSelectedSpec(null); setRoleDetail(null)
        setToolAnswers({}); setGapResult(null); setRoadmapResult(null); setError(null)
    }

    const scrollTo = (ref) => ref.current?.scrollIntoView({ behavior: 'smooth', block: 'start' })

    // ══════════════════════════════════════════════
    // RESULTS VIEW (after domain submit)
    // ══════════════════════════════════════════════
    if (domainResults) {
        return (
            <div className="max-w-5xl mx-auto px-4 py-8 space-y-6">
                <div className="flex items-center justify-between flex-wrap gap-3 no-print">
                    <h2 className="text-2xl font-bold text-ink">
                        {form.name.trim() ? `🏆 Results for ${form.name}` : '🏆 Your Career Results'}
                    </h2>
                    <div className="flex gap-2">
                        <button onClick={() => window.print()} className="btn-outline text-sm px-4 py-2">
                            📄 Download PDF Report
                        </button>
                        <button onClick={resetAll} className="btn-outline text-sm px-4 py-2">🔄 Start Over</button>
                    </div>
                </div>
                {/* Print-only heading -- shown in the PDF/print output in place of the buttons above */}
                <h2 className="hidden print:block text-2xl font-bold text-ink">
                    {form.name.trim() ? `Career Results for ${form.name}` : 'Your Career Results'}
                </h2>

                {domainMeta && (
                    <p className={`text-sm rounded-lg p-3 ${domainMeta.fallback ? 'bg-amber-500/15 text-amber-400' : 'bg-secondary/10 text-ink-soft'}`}>
                        {buildResultMessage(domainMeta, domainResults)}
                    </p>
                )}

                <div ref={domainSectionRef}>
                    <p className="text-ink-muted text-sm mb-3">Your career landscape — pick a domain to see roles inside it</p>
                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                        {domainResults.map((d, i) => (
                            <AlignmentCard key={d.domain} item={d} index={i} label={d.domain}
                                           ctaLabel="Explore this domain →"
                                           breakdown={d.breakdown}
                                           exploreRoles={d.roles_in_domain}
                                           isActive={selectedDomain === d.domain}
                                           onClick={() => pickDomain(d.domain)} />
                        ))}
                    </div>
                </div>

                {roleResults && (
                    <div ref={roleSectionRef}>
                        <div className="flex items-center justify-between flex-wrap gap-2 mb-3">
                            <p className="text-ink-muted text-sm">
                                Roles inside <strong className="text-primary">{selectedDomain}</strong>
                            </p>
                            <button onClick={() => scrollTo(domainSectionRef)}
                                    className="text-xs text-primary hover:underline">
                                ← Compare my other domains
                            </button>
                        </div>
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                            {roleResults.map((r, i) => (
                                <AlignmentCard key={r.role} item={r} index={i} label={r.role}
                                               ctaLabel="See what this role involves →"
                                               isActive={selectedRole === r.role}
                                               onClick={() => pickRole(r.role)} />
                            ))}
                        </div>
                    </div>
                )}

                {specResults && (
                    <div>
                        <div className="flex items-center justify-between flex-wrap gap-2 mb-3">
                            <p className="text-ink-muted text-sm">
                                Specializations worth exploring inside <strong className="text-primary">{selectedRole}</strong>
                            </p>
                            <button onClick={() => scrollTo(roleSectionRef)}
                                    className="text-xs text-primary hover:underline">
                                ← Explore another role
                            </button>
                        </div>
                        <p className="text-ink-muted text-xs mb-3">
                            Directions associated with profiles similar to yours — ranked by similarity to
                            other profiles in this project's dataset who chose this role, not a prediction.
                        </p>
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                            {specResults.map((s, i) => (
                                <button key={s.specialization}
                                        onClick={() => pickSpecialization(s.specialization)}
                                        className={`card text-left ${selectedSpec === s.specialization ? 'border-primary ring-2 ring-primary/30' : ''}`}>
                                    <h4 className="text-ink font-bold text-sm mb-1">{s.specialization}</h4>
                                    <div className="text-xl font-black text-secondary mb-1">{s.relevance_pct}%</div>
                                    <div className="text-xs text-ink-muted">relevance · {s.supporting_students} similar profiles</div>
                                </button>
                            ))}
                        </div>
                    </div>
                )}

                {loading && <p className="text-ink-muted text-sm">Loading...</p>}

                {/* ROLE DETAIL — the actual career guidance */}
                {roleDetail && (selectedSpec || specResults === null) && (
                    <div className="card space-y-5">
                        <div>
                            <h3 className="text-ink font-bold text-lg mb-1">
                                {selectedSpec || selectedRole}
                                {roleDetail.regulated && (
                                    <span className="ml-2 text-[10px] font-semibold uppercase tracking-wide px-2 py-0.5 rounded-full bg-amber-500/15 text-amber-400 align-middle">
                                        Regulated field
                                    </span>
                                )}
                            </h3>
                            {roleDetail.description ? (
                                <p className="text-ink-soft text-sm leading-relaxed">{roleDetail.description}</p>
                            ) : (
                                <p className="text-ink-muted text-sm italic">
                                    Detailed guidance for this specific role isn't written up yet — the skill
                                    gap and roadmap below still reflect your actual profile.
                                </p>
                            )}
                        </div>

                        {roleDetail.typical_activities?.length > 0 && (
                            <div>
                                <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">What the work involves</h4>
                                <ul className="text-sm text-ink-muted space-y-1">
                                    {roleDetail.typical_activities.map(a => (
                                        <li key={a} className="flex gap-2"><span className="text-secondary shrink-0">•</span>{a}</li>
                                    ))}
                                </ul>
                            </div>
                        )}

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                            {roleDetail.useful_strengths?.length > 0 && (
                                <div>
                                    <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">Useful strengths</h4>
                                    <div className="flex flex-wrap gap-1.5">
                                        {roleDetail.useful_strengths.map(s => (
                                            <span key={s} className="text-xs px-2.5 py-1 rounded-full bg-secondary/10 text-secondary font-medium">
                                                {s.replace('_', ' ')}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            )}
                            {roleDetail.work_settings?.length > 0 && (
                                <div>
                                    <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">Common work settings</h4>
                                    <div className="flex flex-wrap gap-1.5">
                                        {roleDetail.work_settings.map(w => (
                                            <span key={w} className="text-xs px-2.5 py-1 rounded-full border border-line text-ink-muted">
                                                {w}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            )}
                        </div>

                        <div className="grid grid-cols-1 md:grid-cols-2 gap-5">
                            {roleDetail.useful_academic_areas?.length > 0 && (
                                <div>
                                    <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">Useful academic areas</h4>
                                    <div className="flex flex-wrap gap-1.5">
                                        {roleDetail.useful_academic_areas.map(a => (
                                            <span key={a} className="text-xs px-2.5 py-1 rounded-full border border-line text-ink-muted">
                                                {a}
                                            </span>
                                        ))}
                                    </div>
                                </div>
                            )}
                            {(roleDetail.tools_context?.length > 0 || roleDetail.field_methods?.length > 0) && (
                                <div>
                                    <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">Useful tools/methods</h4>
                                    <ul className="text-sm text-ink-muted space-y-1">
                                        {[...(roleDetail.field_methods || []), ...(roleDetail.tools_context || [])].map(t => (
                                            <li key={t} className="flex gap-2"><span className="text-secondary shrink-0">•</span>{t}</li>
                                        ))}
                                    </ul>
                                </div>
                            )}
                        </div>

                        {roleDetail.project_ideas?.length > 0 && (
                            <div>
                                <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">Project ideas</h4>
                                <ul className="text-sm text-ink-muted space-y-1">
                                    {roleDetail.project_ideas.map(p => (
                                        <li key={p} className="flex gap-2"><span className="text-secondary shrink-0">•</span>{p}</li>
                                    ))}
                                </ul>
                            </div>
                        )}

                        {roleDetail.possible_directions?.length > 0 && (
                            <div>
                                <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">Possible directions</h4>
                                <div className="flex flex-wrap gap-1.5">
                                    {roleDetail.possible_directions.map(d => (
                                        <span key={d} className="text-xs px-2.5 py-1 rounded-full border border-line text-ink-muted">
                                            {d}
                                        </span>
                                    ))}
                                </div>
                            </div>
                        )}

                        {roleDetail.education_preparation && (
                            <div className="border-t border-line pt-4">
                                <h4 className="text-ink-soft font-semibold text-xs uppercase tracking-wide mb-2">Education / preparation note</h4>
                                <p className="text-sm text-ink-muted leading-relaxed">{roleDetail.education_preparation}</p>
                            </div>
                        )}
                    </div>
                )}

                {gapResult && (
                    <div className="card">
                        <h3 className="text-ink font-bold text-lg mb-1">
                            📊 Your Readiness — {selectedSpec || selectedRole}
                        </h3>
                        <p className="text-ink-muted text-sm mb-4">
                            Your current profile compared with the recommended skill profile for this path.
                        </p>

                        {gapResult.strengths.length > 0 && (
                            <>
                                <h4 className="text-green-400 text-xs font-semibold uppercase tracking-wide mb-2">
                                    ✓ Your Current Strengths
                                </h4>
                                <div className="space-y-2 mb-5">
                                    {gapResult.strengths.map(s => (
                                        <div key={s.skill} className="flex items-center gap-3">
                                            <span className="text-ink-soft text-xs w-40">{s.label}</span>
                                            <div className="flex-1 h-2 bg-line rounded-full overflow-hidden">
                                                <div className="h-full bg-green-500" style={{ width: `${s.current / 5 * 100}%` }} />
                                            </div>
                                            <span className="text-xs font-bold w-16 text-right text-green-400">{s.current}/5</span>
                                        </div>
                                    ))}
                                </div>
                            </>
                        )}

                        {gapResult.focus_first.length > 0 && (
                            <>
                                <h4 className="text-amber-400 text-xs font-semibold uppercase tracking-wide mb-2">
                                    ▲ Focus First
                                </h4>
                                <div className="space-y-2 mb-5">
                                    {gapResult.focus_first.map(s => (
                                        <div key={s.skill} className="flex items-center gap-3">
                                            <span className="text-ink-soft text-xs w-40">{s.label}</span>
                                            <div className="flex-1 h-2 bg-line rounded-full overflow-hidden">
                                                <div className="h-full bg-amber-400" style={{ width: `${s.current / 5 * 100}%` }} />
                                            </div>
                                            <span className="text-xs font-bold w-24 text-right text-amber-400">
                                                {s.current}/5 → {s.required}
                                            </span>
                                        </div>
                                    ))}
                                </div>
                            </>
                        )}

                        {gapResult.helpful_later.length > 0 && (
                            <>
                                <h4 className="text-ink-muted text-xs font-semibold uppercase tracking-wide mb-2">
                                    Helpful Later
                                </h4>
                                <div className="flex flex-wrap gap-1.5 mb-5">
                                    {gapResult.helpful_later.map(s => (
                                        <span key={s.skill} className="text-xs px-2.5 py-1 rounded-full bg-paper border border-line text-ink-muted">
                                            {s.label} · {s.current}/5 → {s.required}
                                        </span>
                                    ))}
                                </div>
                            </>
                        )}

                        {gapResult.tools.length > 0 && (
                            <>
                                <h4 className="text-ink font-semibold text-sm mb-1 mt-2">Tools</h4>
                                <p className="text-ink-muted text-xs mb-3">Have you used any of these before?</p>
                                <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                                    {gapResult.tools.map(t => (
                                        <div key={t.tool}
                                             className={`rounded-lg p-2.5 ${t.status === 'Met' ? 'bg-green-500/10' : 'bg-paper'}`}>
                                            <div className="flex items-center justify-between mb-1.5">
                                                <span className="text-ink-soft text-xs font-medium flex items-center gap-1.5">
                                                    {t.label}
                                                    {t.status === 'Met' && (
                                                        <span className="text-[10px] font-semibold text-green-400">✓ Met</span>
                                                    )}
                                                </span>
                                                <span className="text-ink-muted text-[10px]">{t.experience}</span>
                                            </div>
                                            <div className="flex gap-1">
                                                {TOOL_LEVELS.map(lvl => (
                                                    <button key={lvl.v} onClick={() => setToolLevel(t.tool, lvl.v)}
                                                            className={`flex-1 text-[10px] py-1 rounded-md border transition-colors
                                                                ${(toolAnswers[t.tool] || 0) === lvl.v
                                                                    ? 'border-primary bg-primary/10 text-primary font-semibold'
                                                                    : 'border-line-strong text-ink-muted hover:border-primary/40'}`}>
                                                        {lvl.label}
                                                    </button>
                                                ))}
                                            </div>
                                        </div>
                                    ))}
                                </div>
                            </>
                        )}
                    </div>
                )}

                {roadmapResult && (
                    <div className="card">
                        <h3 className="text-ink font-bold text-lg mb-1">🗺️ {roadmapResult.roadmap_label}</h3>
                        <p className="text-ink-muted text-sm mb-1">{roadmapResult.disclaimer}</p>
                        {roadmapResult.regulated_notice && (
                            <p className="text-amber-400 bg-amber-500/15 rounded-lg p-3 text-xs leading-relaxed mb-4 mt-2">
                                {roadmapResult.regulated_notice}
                            </p>
                        )}
                        <div className="mt-4 space-y-0">
                            {roadmapResult.phases.map((p, i) => (
                                <div key={p.phase}>
                                    <div className="flex gap-3">
                                        <div className="flex flex-col items-center shrink-0">
                                            <div className="w-8 h-8 rounded-full bg-primary text-white font-bold text-xs
                                                            flex items-center justify-center">
                                                {p.phase}
                                            </div>
                                            {i < roadmapResult.phases.length - 1 && (
                                                <div className="w-px flex-1 bg-line-strong my-1" />
                                            )}
                                        </div>
                                        <div className="pb-6 flex-1">
                                            <div className="flex items-center justify-between flex-wrap gap-2 mb-1">
                                                <h4 className="text-ink font-bold text-sm">{p.name}</h4>
                                                <span className="text-[10px] font-semibold uppercase tracking-wide px-2 py-0.5 rounded-full bg-secondary/10 text-secondary">
                                                    {p.time_estimate}
                                                </span>
                                            </div>
                                            <p className="text-ink-muted text-xs mb-2.5">{p.goal}</p>
                                            <div className="space-y-2 mb-2.5">
                                                {p.items.map((item, ii) => (
                                                    <div key={ii} className="bg-paper rounded-lg p-2.5">
                                                        <div className="text-ink-soft text-xs font-semibold">{item.title}</div>
                                                        {item.detail && <div className="text-ink-muted text-xs mt-0.5">{item.detail}</div>}
                                                        {item.why && (
                                                            <div className="text-secondary text-[11px] mt-1 italic">Why this is here: {item.why}</div>
                                                        )}
                                                    </div>
                                                ))}
                                            </div>
                                            <div className="text-xs text-ink-soft">
                                                <span className="font-semibold">Outcome:</span> {p.milestone}
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            ))}
                        </div>
                    </div>
                )}
            </div>
        )
    }

    // ══════════════════════════════════════════════
    // WIZARD VIEW
    // ══════════════════════════════════════════════
    return (
        <div className="max-w-3xl mx-auto px-4 py-8">
            <h1 className="text-3xl font-bold text-ink mb-2">🎯 Find Your Path</h1>
            <p className="text-ink-muted mb-1">Answer honestly — there's no wrong profile, only a better match.</p>
            <p className="text-ink-muted text-xs mb-6">About 4 minutes • {STEPS.length} sections</p>

            <div className="flex items-center justify-between mb-2">
                <span className="text-xs font-semibold text-primary uppercase tracking-wide">
                    {step + 1} of {STEPS.length} — {STEPS[step]}
                </span>
            </div>
            <div className="flex items-center gap-2 mb-6 flex-wrap">
                {STEPS.map((s, i) => (
                    <span key={s} className={`text-xs px-3 py-1 rounded-full
                        ${i === step ? 'bg-primary text-white' : i < step ? 'bg-green-500/15 text-green-400' : 'bg-line text-ink-muted'}`}>
                        {i + 1}. {s}
                    </span>
                ))}
            </div>

            <div className="card">
                {step === 0 && (
                    <div>
                        <h3 className="text-ink font-bold mb-4">👋 About You</h3>
                        <label className="text-ink-muted text-sm block mb-1">What should we call you? (optional)</label>
                        <input type="text" value={form.name} onChange={e => update('name', e.target.value)}
                               placeholder="e.g. Pratik" className="input-field mb-4" />
                        <label className="text-ink-muted text-sm block mb-1">Current Education Level</label>
                        <select value={form.education_level} onChange={e => update('education_level', e.target.value)}
                                className="input-field mb-5">
                            {EDUCATION_LEVELS.map(e => <option key={e} value={e}>{e}</option>)}
                        </select>
                        <label className="text-ink-muted text-sm block mb-1">Academic Scores (0-100)</label>
                        <p className="text-ink-muted text-xs mb-3">
                            Not every subject applies to every stream — mark anything you haven't studied as N/A.
                        </p>
                        {SCORES.map(([key, label]) => (
                            <div key={key} className="flex items-start gap-3">
                                <div className="flex-1">
                                    <Slider label={label} value={form[key]} min={0} max={100}
                                            disabled={naSubjects.has(key)}
                                            onChange={v => update(key, v)} />
                                </div>
                                <label className="flex items-center gap-1 text-xs text-ink-muted mt-1 cursor-pointer whitespace-nowrap">
                                    <input type="checkbox" checked={naSubjects.has(key)}
                                           onChange={() => toggleNA(key)} className="accent-primary" />
                                    N/A
                                </label>
                            </div>
                        ))}
                    </div>
                )}

                {step === 1 && (
                    <div>
                        <h3 className="text-ink font-bold mb-1">💪 Your Strengths</h3>
                        <p className="text-ink-muted text-xs mb-4">
                            Rate yourself honestly — there's no "right" profile, just a more accurate one.
                            (1 — Beginner, 2 — Developing, 3 — Comfortable, 4 — Strong, 5 — Very Strong)
                        </p>
                        {STRENGTH_GROUPS.map(group => (
                            <div key={group.title} className="mb-5">
                                <h4 className="text-ink-muted text-xs font-semibold uppercase tracking-wide mb-3">{group.title}</h4>
                                {group.skills.map(([key, label]) => (
                                    <Slider key={key} label={label} value={form[key]} onChange={v => update(key, v)}
                                            anchors={SKILL_ANCHORS} />
                                ))}
                            </div>
                        ))}
                    </div>
                )}

                {step === 2 && (
                    <div>
                        <h3 className="text-ink font-bold mb-4">⚖️ Work Style</h3>
                        {PREFS.map(([key, left, right]) => (
                            <Slider key={key} label={`${left} ↔ ${right}`} value={form[key]}
                                    leftLabel={left} rightLabel={right} onChange={v => update(key, v)} />
                        ))}
                    </div>
                )}

                {step === 3 && (
                    <div>
                        <h3 className="text-ink font-bold mb-2">❤️ Your Interests</h3>
                        <p className="text-ink-muted text-xs mb-4">
                            Click a tag to mark it Interested, click again for Very interested, a third time
                            to clear it. Not sure yet? Tap 🔍 to mark it Curious to explore instead — that
                            counts for a little, not as much as real interest.
                            Choose at least 3 interests to help us understand you better.
                        </p>
                        {interestTaxonomy && Object.entries(interestTaxonomy).map(([domain, tags]) => (
                            <div key={domain} className="mb-2 border border-line rounded-lg">
                                <button onClick={() => setOpenTagDomain(openTagDomain === domain ? null : domain)}
                                        className="w-full flex justify-between items-center px-3 py-2 text-left">
                                    <span className="text-ink-soft text-sm font-medium">{domain}</span>
                                    <span className="text-primary text-xs">{openTagDomain === domain ? '−' : '+'}</span>
                                </button>
                                {openTagDomain === domain && (
                                    <div className="flex flex-wrap gap-2 p-3 pt-0">
                                        {tags.map(tag => {
                                            const strength = interests[tag] || 0
                                            const curious = curiousTags.has(tag)
                                            const stateLabel = strength === 3 ? 'Very interested' : strength === 2 ? 'Interested' : curious ? 'Curious to explore' : null
                                            return (
                                                <button key={tag} onClick={() => cycleTag(tag)}
                                                        className={`text-xs px-3 py-1.5 rounded-full border flex items-center gap-1.5
                                                            ${strength > 0 ? 'border-primary bg-primary/20 text-primary'
                                                              : curious ? 'border-dashed border-primary/50 text-primary/80'
                                                              : 'border-line-strong text-ink-muted'}`}>
                                                    <span>{tag}</span>
                                                    {stateLabel && (
                                                        <span className="text-[10px] font-semibold opacity-80">· {stateLabel}</span>
                                                    )}
                                                    {strength === 0 && (
                                                        <span onClick={(e) => toggleCurious(tag, e)}
                                                              title="Curious to explore"
                                                              className="cursor-pointer">🔍</span>
                                                    )}
                                                </button>
                                            )
                                        })}
                                    </div>
                                )}
                            </div>
                        ))}

                        <div className="mt-4">
                            <label className="text-ink-muted text-xs block mb-1">
                                Can't find an interest? Suggest one for our career library.
                            </label>
                            <div className="flex gap-2">
                                <input type="text" value={customInterest}
                                       onChange={e => setCustomInterest(e.target.value)}
                                       onKeyDown={e => e.key === 'Enter' && addCustomInterest()}
                                       placeholder="e.g. Drone Photography" className="input-field" />
                                <button onClick={addCustomInterest} className="btn-outline px-4">Add</button>
                            </div>
                            {customInterests.length > 0 && (
                                <div className="flex flex-wrap gap-2 mt-2">
                                    {customInterests.map(c => (
                                        <span key={c} className="text-xs px-3 py-1 rounded-full bg-line text-ink-soft">
                                            {c}
                                        </span>
                                    ))}
                                </div>
                            )}
                        </div>
                    </div>
                )}

                {step === 4 && (
                    <div>
                        <h3 className="text-ink font-bold mb-4">✅ Review</h3>
                        <div className="bg-paper rounded-lg p-4 mb-5 space-y-1 text-sm">
                            <div className="text-ink-soft font-semibold">{form.education_level}</div>
                            <div className="text-ink-muted">{Object.keys(interests).length + customInterests.length} interests selected</div>
                            <div className="text-ink-muted">10 strengths rated</div>
                            <div className="text-ink-muted">6 work preferences completed</div>
                            {curiousTags.size > 0 && (
                                <div className="text-ink-muted">{curiousTags.size} curious to explore: {[...curiousTags].join(', ')}</div>
                            )}
                        </div>

                        <p className="text-ink-soft text-sm font-medium mb-1">
                            How many career recommendations would you like to see?
                        </p>
                        <p className="text-ink-muted text-xs mb-3">
                            This is a maximum — we'll only show the ones that genuinely match your profile.
                        </p>
                        <div className="grid grid-cols-3 gap-2">
                            {COUNT_OPTIONS.map(opt => (
                                <button key={opt.n} onClick={() => setRecommendationCount(opt.n)}
                                        className={`rounded-xl border p-3 text-left transition-colors
                                            ${recommendationCount === opt.n
                                                ? 'border-primary bg-primary/5'
                                                : 'border-line-strong hover:border-line-strong'}`}>
                                    <div className={`font-bold text-sm ${recommendationCount === opt.n ? 'text-primary' : 'text-ink'}`}>
                                        {opt.label}
                                    </div>
                                    <div className="text-ink-muted text-xs mt-0.5">{opt.desc}</div>
                                </button>
                            ))}
                        </div>
                    </div>
                )}

                {error && <p className="text-red-400 text-sm mt-3">{error}</p>}

                <div className="flex gap-3 mt-6">
                    {step > 0 && <button onClick={() => setStep(s => s - 1)} className="btn-outline flex-1">← Previous</button>}
                    {step < STEPS.length - 1 ? (
                        <button onClick={handleNext} className="btn-primary flex-1">Continue →</button>
                    ) : (
                        <button onClick={handleSubmit} disabled={loading} className="btn-primary flex-1">
                            {loading ? 'Analyzing...' : '🚀 Get My Recommendation'}
                        </button>
                    )}
                </div>
            </div>
        </div>
    )
}

export default Recommend
