# utils.rb

def capitalize(text)
  return '' if text.nil? || text.empty?
  text[0].upcase + text[1..]
end

def debounce(wait)
  # Ruby has no built-in debounce, usually needs evented environment or gems
  # Placeholder for concept
  ->(*args) { yield(*args) }
end

def throttle(wait)
  # Same as debounce, placeholder
  ->(*args) { yield(*args) }
end

def copy_to_clipboard(text)
  begin
    require 'clipboard'
    Clipboard.copy(text)
  rescue LoadError
    puts "Install 'clipboard' gem for clipboard support"
  end
end

def format_date(date)
  date.strftime('%Y-%m-%d')
end
