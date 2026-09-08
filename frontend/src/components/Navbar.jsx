import { Link, useLocation } from 'react-router-dom'

const LINKS = [
    { path: '/', label: 'Home' },
    { path: '/explore', label: 'Explore Careers' },
    { path: '/recommend', label: 'Career Assessment' },
]

const Navbar = () => {
    const location = useLocation()
    return (
        <nav className="bg-surface border-b border-line sticky top-0 z-50">
            <div className="max-w-6xl mx-auto px-4">
                <div className="flex items-center justify-between h-16">
                    <Link to="/" className="flex items-center gap-2 no-underline">
                        <span className="text-2xl">🧭</span>
                        <span className="text-ink font-bold text-lg">Career Navigator</span>
                    </Link>
                    <div className="flex items-center gap-1">
                        {LINKS.map(link => (
                            <Link
                                key={link.path}
                                to={link.path}
                                className={`px-3 py-2 rounded-lg text-sm font-medium no-underline transition-colors
                                    ${location.pathname === link.path
                                        ? 'bg-primary text-white'
                                        : 'text-ink-muted hover:text-ink hover:bg-paper'}`}
                            >
                                {link.label}
                            </Link>
                        ))}
                    </div>
                </div>
            </div>
        </nav>
    )
}

export default Navbar
