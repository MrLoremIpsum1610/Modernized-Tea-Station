/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./{*.html,./js/*.js}"],
darkMode: 'class', 

  theme: {
    extend: {
      colors:{
        'btn-color':'#678e3e;',
        'parColor':"#4c667f",
        'bgc-grid':'#f1f5f8',
        'BlackMetalical':'#222'
      },
      letterSpacing:{
        "TeaWide":"0.29rem"
      }
      ,
      screens:{
        'max-ssm':{max:"480px"},
        'max-sm':{max:'640px'},
        'max-md':{max:'768px'},
        'max-lg':{max:'1024px'},
        'max-xl':{max:'1280px'},
        'max-2xl':{max:'1536px'},
      },
      fontSize:{
        "x-8":"32px",
        "x-16":"64px",
        "x-10":"40px",
      },
      spacing:{
        '3.5':"14px",
        '2.5':"10px",
        '18':'72px',
      },
      fontFamily:{
        'grand-hotel': ['"Grand Hotel"', 'cursive'],
        'catmaran': '"Catamaran"',
      },
      animation: {
        bounce: 'Anim__bounce 1s ease-in-out infinite',
        slideFromRight: 'Anim__slideFromRight 0.5s ease-out forwards',
        slideFromLeft: 'Anim__slideFromLeft 0.5s ease-out forwards',
        show: 'Anim__show 1.3s ease-out 1',
      },
      keyframes: {
        Anim__bounce: {
          '0%, 100%': { transform: 'scale(1)' },
          '50%': { transform: 'scale(1.1)' },
        },
        Anim__slideFromRight: {
          '0%': { transform: 'translateX(100px)', opacity: '0' },
          '100%': { transform: 'translateX(0px)', opacity: '1' },
        },
        Anim__slideFromLeft: {
          '0%': { transform: 'translateX(-100px)', opacity: '0' },
          '100%': { transform: 'translateX(0px)', opacity: '1' },
        },
        Anim__show: {
          '0%': { transform: 'scale(0.7)', opacity: '0' },
          '50%': { transform: 'scale(1.3)', opacity: '0.5' },
          '100%': { transform: 'scale(1)', opacity: '1' },
        },
      },
    },
            
  },
  plugins: []
}