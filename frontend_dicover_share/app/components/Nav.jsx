"use client";

import React from 'react';
import Link from 'next/link';
import Image from 'next/image';
import { useState, useEffect } from 'react';

import { useSession, singOut, signIn, getProviders } from "next-auth/react"

const Nav = () => {
  const isUserLoggedIn = true;

  const [providers, setProviders] = useState(null)

  useEffect(() => {
    const setProviders = async () => {
      const response = await getProviders();
      setProviders(response);
    }
  })

  return (

    <nav className='flex justify-between w-full items-center mt-3 mb-16 pt-3 '>

      <Link href="/" className='flex gap-2'>
        <Image
          src="/assets/logo_aperam.png"
          alt="Logo Aperam"
          width={200}
          height={100}
          className='object-contain'
        />
        <div className="sm:"></div>

        <p className='max-sm:hidden  font-semibold text-lg text-black tracking-wide'> Argus </p>

      </Link>


      {/* Desktop navigator */}
      <div className='sm:flex hidden'>
        {isUserLoggedIn ?
          (
          <div className='flex gap-3 md:gap-5'>

            <Link href={"/create-prompt"} 
            className='black_btn'> 
            Create Post 
            </Link>

            <button type='button' 
            onClick={singOut} 
            className='outline_btn'>
            Sign Out
            </button>

            <Link href="/profile">

              <Image
                src={"/assets/logo_aperam.png"}
                width={100}
                height={100}
                className=''
                alt='profile'
              />

            </Link>
          </div>
          ):(<>
          
          {providers && 
            Object.values(providers).map((providers)=> (
                <button
                  type='button'
                  key={provider.name}
                  onClick={()=> signIn (provider.id)}
                  className='black_btn'>
                    Sign In
                </button>
              ))
          }
          </>)}
      </div>


      {/* Mobile navigator */}

      <div className='sm:hidden flex relative'></div>


    </nav>

  )
}

export default Nav
