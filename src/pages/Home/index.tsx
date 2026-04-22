import { useEffect } from 'react'
import { useSearchParams } from 'react-router-dom'
import Hero from './Hero'
import Technologies from './Technologies'
import ChooseWeapon from './ChooseWeapon'
import AboutUs from './AboutUs'
import Vacancies from './Vacancies'

export default function Home() {
  const [searchParams] = useSearchParams()

  useEffect(() => {
    if (searchParams.get('scroll') === 'vacancies') {
      setTimeout(() => {
        document.getElementById('vacancies')?.scrollIntoView({ behavior: 'smooth' })
      }, 100)
    }
  }, [searchParams])

  return (
    <div>
      <Hero />
      <Technologies />
      <ChooseWeapon />
      <AboutUs />
      <Vacancies />
    </div>
  )
}
