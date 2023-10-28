import { useState } from 'react'
import { Container } from 'react-bootstrap'
import viteLogo from '/vite.svg'
import './App.css'
import './bootstrap.min.css'
import Header from './components/Header'
import Footer from './components/Footer'

function App() {
  return (
    <>
      <Header />
      <main className='py-3'>
        <Container>
          <h1>Welcome</h1>
        </Container>
        
      </main>
      <Footer />
    </>
  )
}

export default App
