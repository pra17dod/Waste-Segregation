import React from 'react';

export default function Navbar() {
  return (
    <div>
        <header role="banner" class="ui-section-header">
        <div class="ui-layout-container">
            <div class="ui-section-header__layout ui-layout-flex">
        
            <a href="#" role="link" aria-label="#" class="ui-section-header--logo">
                <img width="60" src="https://cdn.dribbble.com/users/179241/screenshots/6116810/chris-fernandez-electric-recycling-editorial-1-dribbble.png" />
            </a>
            <input type="checkbox" id="ui-section-header--menu-id" />
            <label for="ui-section-header--menu-id" class="ui-section-header--menu-icon"></label>
            
            <nav role="navigation" class="ui-section-header--nav ui-layout-flex">
                <a href="#" role="link" aria-label="#" class="ui-section-header--nav-link">Home</a>
                <a href="http://indiawastemanagementportal.org/" role="link" aria-label="#" class="ui-section-header--nav-link">MoreInfo</a>
                <a href="https://github.com/pra17dod/Waste-Segregation" role="link" aria-label="#" class="ui-section-header--nav-link">GitHub</a>
            </nav>
            </div>
        </div>
        </header>
    </div>
  );
}

