import { useState, useEffect } from 'react'
import api from '../api/axiosConfig'

const ModelPerformance = () => {
    const [domainModel, setDomainModel] = useState(null)
    const [roleModels, setRoleModels] = useState(null)
    const [clusters, setClusters] = useState(null)

    useEffect(() => {
        api.get('/api/ml/domain-model').then(r => setDomainModel(r.data))
        api.get('/api/ml/role-models').then(r => setRoleModels(r.data.role_models))
        api.get('/api/ml/clusters').then(r => setClusters(r.data.clusters))
    }, [])

    if (!domainModel) return <div className="text-center py-20 text-ink-muted">Loading...</div>

    const randomBaseline = Math.round(100 / domainModel.domain_count)

    return (
        <div className="max-w-5xl mx-auto px-4 py-8 space-y-8">
            <h1 className="text-3xl font-bold text-ink">🤖 Model Performance</h1>

            <div className="card">
                <h3 className="text-ink font-bold mb-2">Level 1 — Domain Model (Random Forest)</h3>
                <p className="text-ink-muted text-xs mb-4">
                    Predicts which of 13 broad career domains fits a student, from academics,
                    skills, preferences, and interest-tag aggregates.
                </p>
                <div className="flex items-end gap-6 mb-4">
                    <div>
                        <div className="text-4xl font-black text-primary">{domainModel.accuracy}%</div>
                        <div className="text-ink-muted text-xs">accuracy on held-out test data</div>
                    </div>
                    <div className="text-ink-muted text-xs">
                        vs. {randomBaseline}% random-guess baseline across {domainModel.domain_count} classes —
                        roughly {(domainModel.accuracy / randomBaseline).toFixed(1)}x better than chance
                    </div>
                </div>
                <h4 className="text-ink-soft text-sm font-semibold mb-2">Top contributing features</h4>
                <div className="space-y-1">
                    {domainModel.top_features.slice(0, 8).map(([name, val]) => (
                        <div key={name} className="flex items-center gap-2">
                            <span className="text-ink-muted text-xs w-56 truncate">{name}</span>
                            <div className="flex-1 h-2 bg-line rounded-full overflow-hidden">
                                <div className="h-full bg-secondary" style={{ width: `${val * 100 * 6}%` }} />
                            </div>
                        </div>
                    ))}
                </div>
            </div>

            <div className="card">
                <h3 className="text-ink font-bold mb-2">Level 2 — Role Models (cascade, one per domain)</h3>
                <p className="text-ink-muted text-xs mb-4">
                    A separate Random Forest per domain, trained only on that domain's students.
                    Distinguishing adjacent real careers (e.g. Nurse vs. Pharmacist) is a genuinely
                    harder problem than domain-level fit — these numbers reflect that honestly.
                </p>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-2">
                    {roleModels && roleModels.map(rm => (
                        <div key={rm.domain} className="bg-paper rounded-lg p-3 flex justify-between items-center">
                            <span className="text-ink-soft text-xs">{rm.domain}</span>
                            {rm.trained ? (
                                <span className="text-primary text-sm font-bold">{rm.accuracy}%</span>
                            ) : (
                                <span className="text-ink-muted text-xs">not enough data</span>
                            )}
                        </div>
                    ))}
                </div>
            </div>

            <div className="card">
                <h3 className="text-ink font-bold mb-2">K-Means — Student Archetypes</h3>
                <p className="text-ink-muted text-xs mb-4">
                    Unsupervised clustering by skill profile alone (no domain/role labels used) —
                    an exploratory view of natural student groupings, not part of the recommendation itself.
                </p>
                <div className="grid grid-cols-1 md:grid-cols-3 gap-3">
                    {clusters && clusters.map(c => (
                        <div key={c.cluster_id} className="bg-paper rounded-lg p-3">
                            <div className="text-ink font-bold text-sm mb-1">Cluster {c.cluster_id + 1}</div>
                            <div className="text-ink-muted text-xs mb-2">{c.student_count} students</div>
                            <div className="text-xs text-ink-muted">
                                Top domains: {Object.keys(c.top_domains).join(', ')}
                            </div>
                        </div>
                    ))}
                </div>
            </div>
        </div>
    )
}

export default ModelPerformance
