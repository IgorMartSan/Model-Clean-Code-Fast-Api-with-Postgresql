
interface LayoutProps {
    titulo: string
    subtitulo: string
    children?: any
}

export default function Header(props: LayoutProps) {
    return (
        <>
            {/* Header */}
            <header className="bg-gradient-to-r from-orange-500 to-orange-700 text-white py-4 px-8">
                igor
            </header>
        </>
    )

}