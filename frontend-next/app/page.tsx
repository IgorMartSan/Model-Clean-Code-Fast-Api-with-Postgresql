import Image from "next/image";


export default function Home() {
  return (
   
    <div className="flex flex-col h-screen">
      {/* Header */}
      <header className="bg-gradient-to-r from-orange-500 to-orange-700 text-white py-4 px-8">
        Header
      </header>
      <div className="flex h-screen">
   
      {/* Navigation */}
      <nav className="bg-gray-200 py-4 px-8 overflow-auto hover:overflow-scroll">
        Navigation
      </nav>


      {/* Main Content */}
      <main className="flex-1 bg-gray-400 py-8 px-8">
        Main Content
      </main>
      </div>
      {/* Footer */}
      <footer className="bg-gray-200 py-4 px-8">
        Footer
      </footer>
    </div>
  );
}
