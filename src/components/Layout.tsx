import { Outlet } from 'react-router-dom'
import Header from './Header'
import Footer from './Footer'

export default function Layout() {
  return (
    <div className="overflow-x-hidden bg-[--main-black]">
      <Header />
      <main className="w-full h-full">
        <Outlet />
      </main>
      <Footer />
    </div>
  )
}
