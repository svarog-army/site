import { useTranslation } from 'react-i18next'
import { LINKS } from '../config'

interface Props {
  className?: string
}

export default function SupportButton({ className = '' }: Props) {
  const { t } = useTranslation()
  return (
    <>
      <a
        href={LINKS.donate}
        target="_blank"
        rel="noreferrer"
        className={`relative inline-flex md:hidden items-center justify-start py-3 px-12 overflow-hidden font-semibold text-white transition-all duration-150 ease-in-out bg-[--main-grey-opacity] group ${className}`}
      >
        <span className="absolute bottom-0 left-0 w-full h-1 transition-all duration-150 ease-in-out bg-[--main-green] group-hover:h-full" />
        <span className="absolute bottom-0 left-0 w-full h-1 transition-all duration-150 ease-in-out bg-[--main-green] group-hover:bg-[--main-grey]" />
        <span className="relative w-full text-center text-base text-[--main-white-87] transition-colors duration-200 ease-in-out group-hover:text-black">
          {t('donate.toSupport')}
        </span>
      </a>
      <a
        href={LINKS.donate}
        target="_blank"
        rel="noreferrer"
        className={`relative hidden md:inline-flex items-center justify-start py-3 px-12 overflow-hidden font-semibold text-white transition-all duration-150 ease-in-out bg-[--main-grey-opacity] group ${className}`}
        style={{ clipPath: 'polygon(0 0, 100% 0, 80% 100%, 0% 100%)' }}
      >
        <span
          className="absolute bottom-0 left-0 h-full w-1 transition-all duration-150 ease-in-out bg-[--main-grey] group-hover:w-full"
          style={{ clipPath: 'polygon(0 0, 100% 0, 80% 100%, 0% 100%)' }}
        />
        <span className="absolute bottom-0 left-0 h-full w-1 transition-all duration-150 ease-in-out bg-[--main-grey] group-hover:bg-[#D71E1E]" />
        <span className="relative right-4 w-full text-center text-base text-[--main-white-87] transition-colors duration-200 ease-in-out group-hover:text-black">
          {t('donate.toSupport')}
        </span>
      </a>
    </>
  )
}
