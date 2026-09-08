import { useState, useEffect } from 'react'
import api from '../api/axiosConfig'

const DataAnalysis = () => {
    const [summary, setSummary] = useState(null)
    const [domains, setDomains] = useState(null)
    const [skills, setSkills] = useState(null)

    useEffect(() => {
        api.get('/api/eda/summary').then(r => setSummary(r.data))
        api.get('/api/eda/domains').then(r => setDomains(r.data.data))
        api.get('/api/eda/skills').then(r => setSkills(r.data.data))
    }, [])

    if (!summary) return <div className="text-center py-20 text-ink-muted">Loading...</div>

    return (
        <div className="max-w-5xl mx-auto px-4 py-8 space-y-8">
            <h1 className="text-3xl font-bold text-ink">📊 Data Analysis</h1>

            <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
                {[
                    ['Students', summary.total_students], ['Domains', summary.domain_count],
                    ['Roles', summary.role_count], ['Specializations', summary.specialization_count],
                ].map(([label, val]) => (
                    <div key={label} className="metric-card">
                        <div className="text-2xl font-bold text-primary">{val}</div>
                        <div className="text-ink-muted text-xs">{label}</div>
                    </div>
                ))}
            </div>

            <div className="card">
                <h3 className="text-ink font-bold mb-4">Students per Domain</h3>
                <p className="text-ink-muted text-xs mb-4">
                    Why this matters: the ML models need enough examples per class to learn
                    reliably — this shows exactly how much data backs each domain's prediction.
                </p>
                <div className="space-y-2">
                    {domains && domains.map(d => (
                        <div key={d.domain} className="flex items-center gap-3">
                            <span className="text-ink-soft text-xs w-56 truncate">{d.domain}</span>
                            <div className="flex-1 h-3 bg-line rounded-full overflow-hidden">
                                <div className="h-full bg-primary" style={{ width: `${d.percentage * 3}%` }} />
                            </div>
                            <span className="text-ink-muted text-xs w-16 text-right">{d.count} ({d.percentage}%)</span>
                        </div>
                    ))}
                </div>
            </div>

            <div className="card overflow-x-auto">
                <h3 className="text-ink font-bold mb-2">Average Skill Profile by Domain</h3>
                <p className="text-ink-muted text-xs mb-4">
                    Why this matters: this is literally what the Domain model learns from —
                    domains with clearly different skill averages are easier to predict correctly.
                </p>
                <table className="w-full text-xs text-left">
                    <thead>
                        <tr className="text-ink-muted border-b border-line">
                            <th className="py-2 pr-4">Domain</th>
                            {skills && Object.keys(skills[0]).filter(k => k !== 'domain').map(k => (
                                <th key={k} className="py-2 px-2">{k.replace('_', ' ')}</th>
                            ))}
                        </tr>
                    </thead>
                    <tbody>
                        {skills && skills.map(row => (
                            <tr key={row.domain} className="border-b border-line">
                                <td className="py-2 pr-4 text-ink-soft">{row.domain}</td>
                                {Object.entries(row).filter(([k]) => k !== 'domain').map(([k, v]) => (
                                    <td key={k} className="py-2 px-2 text-ink-muted">{v}</td>
                                ))}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <div className="card border-amber-300 bg-amber-50">
                <h3 className="text-amber-800 font-bold mb-2">⚠️ About this data</h3>
                <p className="text-ink-muted text-sm">
                    This dataset is <strong>synthetic</strong> — generated from hand-authored domain/role
                    profiles with random noise, not real student survey data. It exists to build and test
                    the ML pipeline end to end. Before real deployment, Domain/Role skill requirements
                    should be validated against real outcome data (student surveys, or public occupational
                    data such as O*NET).
                </p>
            </div>
        </div>
    )
}

export default DataAnalysis
