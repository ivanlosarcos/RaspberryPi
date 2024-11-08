import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter, Link } from 'react-router-dom';


export default function Home() {
  return (
    <div className="grid grid-rows-[20px_1fr_20px] items-center justify-items-center min-h-screen p-8 pb-20 gap-16 sm:p-20 font-[family-name:var(--font-geist-sans)]">
      <h1>Welcome to my Raspberry Pi</h1>
      <p>
        Click <Link to="/stats" className="text-blue-500 hover:underline">here</Link> to see the stats of the device.
      </p>
    </div>
  )
}