fetch('events.json')
  .then(res => res.json())
  .then(events => {
    const container = document.getElementById('events-container');
    container.innerHTML = ''; // Clear "Loading..." text

    // Filter for today and future events
    const today = new Date();
    today.setHours(0, 0, 0, 0);

    const filteredEvents = events.filter(event => {
      const eventDate = new Date(event.date);
      eventDate.setHours(0, 0, 0, 0);
      return eventDate >= today;
    });

    // Sort by date ascending
    filteredEvents.sort((a, b) => new Date(a.date) - new Date(b.date));

    // Show only up to 3 events
    const eventsToShow = filteredEvents.slice(0, 3);

    if (eventsToShow.length === 0) {
      container.innerHTML = '<p>No events announced yet!</p>';
      return;
    }

    const list = document.createElement('ul');
    list.style.listStyle = 'square';

    eventsToShow.forEach(event => {
      const item = document.createElement('li');
      item.innerHTML = `<strong>${event.title}</strong> - ${event.date} @ ${event.location}<br><em>${event.description}</em>`;
      list.appendChild(item);
    });

    container.appendChild(list);
  })
  .catch(err => {
    document.getElementById('events-container').innerHTML = `<p>Couldn't load events. Try again later.</p>`;
    console.error('Error loading events:', err);
  });
