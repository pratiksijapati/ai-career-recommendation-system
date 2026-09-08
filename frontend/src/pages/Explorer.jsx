import { useState, useEffect } from 'react'
import api from '../api/axiosConfig'

const Explorer = () => {
    const [taxonomy, setTaxonomy] = useState(null)
    const [openDomain, setOpenDomain] = useState(null)
    const [openRole, setOpenRole] = useState(null)

    useEffect(() => {
        api.get('/api/explorer/taxonomy').then(res => setTaxonomy(res.data.taxonomy))
    }, [])

    if (!taxonomy) return <div className="text-center py-20 text-ink-muted">Loading...</div>

    return (
        <div className="max-w-5xl mx-auto px-4 py-8">
            <h1 className="text-3xl font-bold text-ink mb-2">🗺️ Explore Careers</h1>
            <p className="text-ink-muted mb-8">
                Browse every career field we track — no quiz needed. Click a domain to see its roles.
            </p>

            <div className="space-y-3">
                {Object.entries(taxonomy).map(([domain, ddata]) => (
                    <div key={domain} className="card">
                        <button
                            onClick={() => { setOpenDomain(openDomain === domain ? null : domain); setOpenRole(null) }}
                            className="w-full flex items-center justify-between text-left"
                        >
                            <div>
                                <h2 className="text-ink font-bold">{domain}</h2>
                                <p className="text-ink-muted text-xs">
                                    {Object.keys(ddata.roles).length} roles
                                    {!ddata.expandable && ' · full specialization detail available'}
                                </p>
                            </div>
                            <span className="text-primary text-xl">{openDomain === domain ? '−' : '+'}</span>
                        </button>

                        {openDomain === domain && (
                            <div className="mt-4 space-y-2 border-t border-line pt-4">
                                {Object.entries(ddata.roles).map(([role, rdata]) => {
                                    const specs = Object.entries(rdata.specializations || {})
                                    return (
                                        <div key={role} className="bg-paper rounded-lg p-3">
                                            <button
                                                onClick={() => setOpenRole(openRole === role ? null : role)}
                                                className="w-full flex items-center justify-between text-left"
                                                disabled={specs.length === 0}
                                            >
                                                <span className="text-ink text-sm font-medium">{role}</span>
                                                {specs.length > 0 && (
                                                    <span className="text-primary text-xs">
                                                        {openRole === role ? '− hide' : `+ ${specs.length} specializations`}
                                                    </span>
                                                )}
                                            </button>
                                            {openRole === role && specs.length > 0 && (
                                                <div className="mt-3 grid grid-cols-1 md:grid-cols-2 gap-2">
                                                    {specs.map(([spec, sdata]) => {
                                                        const subs = sdata.sub_specializations
                                                        return (
                                                            <div key={spec} className="border border-line-strong rounded-lg p-2 bg-surface">
                                                                <div className="text-xs font-semibold text-ink-soft mb-1">{spec}</div>
                                                                {subs ? (
                                                                    <ul className="text-xs text-ink-muted space-y-0.5">
                                                                        {Object.entries(subs).map(([sub, subdata]) => (
                                                                            <li key={sub}>
                                                                                <span className="text-ink-soft">{sub}:</span>{' '}
                                                                                {subdata.technologies?.join(', ')}
                                                                            </li>
                                                                        ))}
                                                                    </ul>
                                                                ) : (
                                                                    <div className="text-xs text-ink-muted">
                                                                        {sdata.technologies?.join(', ')}
                                                                    </div>
                                                                )}
                                                            </div>
                                                        )
                                                    })}
                                                </div>
                                            )}
                                        </div>
                                    )
                                })}
                            </div>
                        )}
                    </div>
                ))}
            </div>
        </div>
    )
}

export default Explorer
