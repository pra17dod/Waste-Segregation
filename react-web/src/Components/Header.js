import React, {useState, useEffect} from 'react';
import { Cloudinary } from 'cloudinary-core';

export default function Header() {

	const [loading, setLoading] = useState(false);
	const [image, setImage] = useState(null);
	const [imageURL, setImageURL] = useState("");

	const uploadImage = async e => {
		const files = e.target.files
		const data = new FormData()
		data.append('file',files[0])
		data.append('upload_preset', 'wasteimages')
		setLoading(true)

		const res1 = await fetch("https://api.cloudinary.com/v1_1/neel0506/image/upload", {
			method: 'POST',
			body: data
		})

		const file = await res1.json()
		console.log("Image Uploaded:");
		console.log(file.secure_url);
		setImageURL(file.secure_url);

		fetch('https://af9042c910f6.ngrok.io/predict', {
			method: 'POST',
			headers: {
				'Content-type': 'application/json',
			},
			body: JSON.stringify({
				"image" : "https://res.cloudinary.com/neel0506/image/upload/v1615671506/wasteimages/xdjrpknzvsvw9pxujdmd.jpg"
			})
		})
		.then(res => res.json())
		.then(data => {
			console.log(data);
			setImage(data.predict)	
			setLoading(false)
		});

	}

	function refreshPage() {
		window.location.reload(false);
	}

	return (
    	<div>
        	<section class="ui-section-hero">
        	<div class="ui-layout-container">
          		<div class="ui-section-hero__layout ui-layout-grid ui-layout-grid-2">
            		<div>
            		<h1>Waste Segregation</h1>
              		<p class="ui-text-intro">We know that your life is of no value but the life of our planet does! So, help us segregate waste according to the category.</p>
              
              		<div class="ui-component-cta ui-layout-flex">
           
						<input type="file" id="InputFile" name = "file"
							onChange={uploadImage} />

                  		<button onClick={refreshPage} className="display-button">Reset</button>
              		</div>
            	</div>
            
            	<img src="https://cdn.dribbble.com/users/1068771/screenshots/8801476/media/517d9a1e6d85d294d5daa0a870633994.jpg" />
        	</div>
			<div>
				{
					loading ? (
						<img className="loading-gif" src="https://cdn.dribbble.com/users/227188/screenshots/6792663/recycle.gif" />
					) : (
						<div className="display-image">
							<img className="waste-image" src={imageURL} />
						</div>
					)
				}
			<p>{image}</p>

			</div>
        </div>
    	</section> 
    </div>
  );
}

