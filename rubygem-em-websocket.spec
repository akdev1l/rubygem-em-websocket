# Generated from em-websocket-0.5.1.gem by gem2rpm -*- rpm-spec -*-
%global gem_name em-websocket

Name: rubygem-%{gem_name}
Version: 0.5.1
Release: 1%{?dist}
Summary: EventMachine based WebSocket server
License: MIT
URL: http://github.com/igrigorik/em-websocket
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
BuildRequires: rubygem(rspec)
BuildRequires: rubygem(em-spec)
BuildRequires: rubygem(http_parser.rb)
BuildArch: noarch

%description
EventMachine based WebSocket server.


%package doc
Summary: Documentation for %{name}
Requires: %{name} = %{version}-%{release}
BuildArch: noarch

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/



%check
pushd .%{gem_instdir}
# we do not have packages needed for tests in fedora
sed -i '/em-http/ s/^/#/' spec/helper.rb
sed -i '/em-websocket-client/ s/^/#/' spec/helper.rb

mv spec/integration/common_spec.rb{,.bak}
mv spec/integration/draft75_spec.rb{,.bak}

rspec spec
popd

%files
%dir %{gem_instdir}
%exclude %{gem_instdir}/.gitignore
%exclude %{gem_instdir}/em-websocket.gemspec
%{gem_libdir}
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/CHANGELOG.rdoc
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/examples
%{gem_instdir}/spec

%changelog
* Wed Jan 24 2018 Jaroslav Prokop <jar.prokop@volny.cz> - 0.5.1-1
- Initial package
