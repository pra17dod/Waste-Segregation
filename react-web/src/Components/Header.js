import React from 'react';

export default function Header() {
  return (
    <div>
        <section class="ui-section-hero">
        <div class="ui-layout-container">
          <div class="ui-section-hero__layout ui-layout-grid ui-layout-grid-2">
 
            <div>
              <h1>Waste Segregation</h1>
              <p class="ui-text-intro">We know that your life is of no value but the life of our planet does! So, help us segregate waste according to the category.</p>
              
              <div class="ui-component-cta ui-layout-flex">
                <a href="#" class="ui-component-button ui-component-button-normal ui-component-button-primary">Open Camera</a>
                <p class="ui-text-note"><small>Scan your waste/face.</small></p>
              </div>
            </div>
            
            <img src="https://cdn.dribbble.com/users/1068771/screenshots/8801476/media/517d9a1e6d85d294d5daa0a870633994.jpg" />
          </div>
        </div>
      </section>
    </div>
  );
}

