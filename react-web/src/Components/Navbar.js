import React from 'react';

export default function Navbar() {
  return (
    <div>
        <header role="banner" class="ui-section-header">
        <div class="ui-layout-container">
            <div class="ui-section-header__layout ui-layout-flex">
        
            <a href="#" role="link" aria-label="#" class="ui-section-header--logo">
                <img width="60" src="https://cdn.dribbble.com/users/227188/screenshots/6792663/recycle.gif" />
            </a>
            
            <input type="checkbox" id="ui-section-header--menu-id" />
            <label for="ui-section-header--menu-id" class="ui-section-header--menu-icon"></label>
            
            <nav role="navigation" class="ui-section-header--nav ui-layout-flex">
                <a href="#" role="link" aria-label="#" class="ui-section-header--nav-link">Prance</a>
                <a href="#" role="link" aria-label="#" class="ui-section-header--nav-link">Thakker</a>
                <a href="#" role="link" aria-label="#" class="ui-section-header--nav-link">Smiley</a>
            </nav>
            </div>
        </div>
        </header>
    </div>
  );
}

