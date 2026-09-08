import { BrowserRouter, Routes, Route } from 'react-router-dom'
import Navbar from './components/Navbar'
import Home from './pages/Home'
import Explorer from './pages/Explorer'
import Recommend from './pages/Recommend'
import DataAnalysis from './pages/DataAnalysis'
import ModelPerformance from './pages/ModelPerformance'

function App() {
    return (
        <BrowserRouter>
            <div className="min-h-screen bg-paper">
                <Navbar />
                <Routes>
                    <Route path="/" element={<Home />} />
                    <Route path="/explore" element={<Explorer />} />
                    <Route path="/recommend" element={<Recommend />} />
                    <Route path="/data" element={<DataAnalysis />} />
                    <Route path="/models" element={<ModelPerformance />} />
                </Routes>
            </div>
        </BrowserRouter>
    )
}

export default App
